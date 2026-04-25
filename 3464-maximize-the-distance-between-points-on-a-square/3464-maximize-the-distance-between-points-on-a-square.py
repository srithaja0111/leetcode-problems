class Solution:
    def maxDistance(self, side: int, points: list[list[int]], k: int) -> int:
        # 1. Unroll the square boundary into a 1D line [0, 4*side]
        unrolled = []
        for x, y in points:
            if y == 0:          # Bottom edge
                d = x
            elif x == side:     # Right edge
                d = side + y
            elif y == side:     # Top edge
                d = 2 * side + (side - x)
            else:               # Left edge (x == 0)
                d = 3 * side + (side - y)
            unrolled.append(d)
        
        unrolled.sort()
        n = len(unrolled)
        
        # To handle the "circular" nature, we double the array
        extended = unrolled + [d + 4 * side for d in unrolled]

        def can_place(dist):
            # We only need to try starting from points that could be the 1st element
            # in the first 'gap' to cover all circular possibilities.
            # Optimization: Checking starts within the first point's range is enough.
            for i in range(n):
                # If we've passed the distance of the first gap, 
                # we don't need to check further starts
                if unrolled[i] > unrolled[0] + dist:
                    break
                
                count = 1
                last_pos = extended[i]
                limit = extended[i] + 4 * side
                
                curr_idx = i
                for _ in range(k - 1):
                    target = last_pos + dist
                    # Binary search for the next point at least 'dist' away
                    import bisect
                    next_idx = bisect.bisect_left(extended, target, curr_idx + 1)
                    
                    if next_idx < len(extended) and extended[next_idx] < limit:
                        last_pos = extended[next_idx]
                        curr_idx = next_idx
                        count += 1
                    else:
                        break
                
                # After picking k points, the distance between the last and first
                # must also be >= dist to satisfy the circular constraint
                if count == k and (extended[i] + 4 * side - last_pos) >= dist:
                    return True
            return False

        # 2. Binary Search for the maximum possible minimum distance
        low = 1
        high = side
        ans = 0
        
        while low <= high:
            mid = (low + high) // 2
            if can_place(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
                
        return ans