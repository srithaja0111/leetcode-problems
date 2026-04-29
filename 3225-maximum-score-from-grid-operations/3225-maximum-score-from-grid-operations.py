class Solution:
    def maximumScore(self, grid: list[list[int]]) -> int:
        n = len(grid)
        
        # Precompute prefix sums for each column to quickly calculate 
        # the sum of a range of white cells.
        pref = [[0] * (n + 1) for _ in range(n)]
        for j in range(n):
            for i in range(n):
                pref[j][i + 1] = pref[j][i] + grid[i][j]

        # memoization table: dp[col][prev_height][is_less]
        # is_less: 0 if prev_height >= height of col-2, 1 if prev_height < height of col-2
        memo = {}

        def solve(col, prev_h, is_less):
            state = (col, prev_h, is_less)
            if state in memo:
                return memo[state]
            
            if col == n:
                return 0
            
            res = 0
            # Try every possible height for the current column
            for curr_h in range(n + 1):
                score = 0
                
                if curr_h > prev_h:
                    # Current column is taller than previous.
                    # Previous column (white cells) gets score from current column's black cells.
                    # We only add the sum of grid[prev_h...curr_h-1][col-1]
                    if col > 0:
                        # If is_less was 0, it means the column before prev (col-2) 
                        # was already shorter than prev_h, so we don't double count.
                        if is_less == 0:
                            score = pref[col-1][curr_h] - pref[col-1][prev_h]
                
                elif curr_h < prev_h:
                    # Current column is shorter than previous.
                    # Current column (white cells) gets score from previous column's black cells.
                    score = pref[col][prev_h] - pref[col][curr_h]
                
                # Recursive step
                # next_is_less is true if curr_h < prev_h
                res = max(res, score + solve(col + 1, curr_h, 1 if curr_h < prev_h else 0))
            
            memo[state] = res
            return res

        # Start from column 0. prev_h is 0, is_less is 0.
        return solve(0, 0, 0)