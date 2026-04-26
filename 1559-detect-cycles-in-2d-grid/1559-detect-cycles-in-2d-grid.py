class Solution:
    def containsCycle(self, grid: list[list[str]]) -> bool:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()

        def dfs(r, c, pr, pc, char):
            visited.add((r, c))
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == char:
                    # If the neighbor is visited and NOT the parent, we found a cycle!
                    if (nr, nc) in visited and (nr, nc) != (pr, pc):
                        return True
                    
                    # If not visited, continue DFS
                    if (nr, nc) not in visited:
                        if dfs(nr, nc, r, c, char):
                            return True
            
            return False

        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visited:
                    # Start DFS; parent is initialized as (-1, -1)
                    if dfs(r, c, -1, -1, grid[r][c]):
                        return True
                        
        return False