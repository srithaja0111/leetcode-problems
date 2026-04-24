class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        # Count the occurrences of each character
        l_count = moves.count('L')
        r_count = moves.count('R')
        underscore_count = moves.count('_')
        
        # The furthest distance is the absolute difference between L and R,
        # plus the total number of underscores (acting as the dominant direction).
        return abs(l_count - r_count) + underscore_count

# Example Usage:
# sol = Solution()
# print(sol.furthestDistanceFromOrigin("L_RL__R")) # Output: 3
        