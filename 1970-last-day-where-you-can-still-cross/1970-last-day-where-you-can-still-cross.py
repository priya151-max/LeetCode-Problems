from collections import deque

class Solution:
    def latestDayToCross(self, row: int, col: int, cells: list[list[int]]) -> int:
        
        def can_cross(day):
            grid = [[0] * col for _ in range(row)]
            
            # mark water
            for i in range(day):
                r, c = cells[i]
                grid[r-1][c-1] = 1
            
            queue = deque()
            
            # start from top row
            for j in range(col):
                if grid[0][j] == 0:
                    queue.append((0, j))
                    grid[0][j] = 1  # mark visited
            
            directions = [(1,0), (-1,0), (0,1), (0,-1)]
            
            while queue:
                r, c = queue.popleft()
                
                if r == row - 1:
                    return True
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    
                    if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 0:
                        grid[nr][nc] = 1
                        queue.append((nr, nc))
            
            return False
        
        left, right = 1, len(cells)
        ans = 0
        
        while left <= right:
            mid = (left + right) // 2
            
            if can_cross(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return ans