class Solution:
    def maxPathScore(self, grid: list[list[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        
        # dp[i][j][c] = max score at (i, j) with cost c
        # Initialize with -1 to represent unreachable states
        dp = [[[-1] * (k + 1) for _ in range(n)] for _ in range(m)]
        
        # Starting point (0, 0) - grid[0][0] is always 0 per constraints
        dp[0][0][0] = 0
        
        for i in range(m):
            for j in range(n):
                # Calculate cost and score for the current cell
                val = grid[i][j]
                cell_cost = 1 if val > 0 else 0
                cell_score = val
                
                for c in range(k + 1):
                    # If we can't reach this cost at this cell, skip
                    if dp[i][j][c] == -1:
                        continue
                    
                    # Try moving Right
                    if j + 1 < n:
                        new_cost = c + (1 if grid[i][j+1] > 0 else 0)
                        if new_cost <= k:
                            dp[i][j+1][new_cost] = max(
                                dp[i][j+1][new_cost], 
                                dp[i][j][c] + grid[i][j+1]
                            )
                            
                    # Try moving Down
                    if i + 1 < m:
                        new_cost = c + (1 if grid[i+1][j] > 0 else 0)
                        if new_cost <= k:
                            dp[i+1][j][new_cost] = max(
                                dp[i+1][j][new_cost], 
                                dp[i][j][c] + grid[i+1][j]
                            )
        
        # The answer is the maximum score in the last cell for any cost <= k
        ans = max(dp[m-1][n-1])
        return ans if ans != -1 else -1