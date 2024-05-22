from collections import deque
from typing import List


class Solution:
    #def __init__(self):

    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols=len(grid[0])
        visited = set()
        mins=-1

        self.freshoranges = 0


        def bfs(row,col,mins):
            queue = deque()
            queue.append((row,col,mins))
            directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
            while queue:
                r,c,m=queue.popleft()
                m=m+1
                for i,j in directions:
                    r1=r+i
                    c1=c+j
                    if r1 in range(rows) and c1 in range(cols) and grid[r1][c1]==1 and (r1,c1) not in visited:
                        self.freshoranges -=1
                        grid[r1][c1]=2
                        queue.append((r1,c1,m))
                        visited.add((r1,c1))
            return m




        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    self.freshoranges+=1
                elif grid[i][j]==2 and grid[i][j] not in visited:
                    mins = bfs(i,j,mins)
                    visited.add((i,j))
        return mins if self.freshoranges ==0 else -1



listoranges = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
sol = Solution()
answer = sol.orangesRotting(listoranges)
print("result ", answer)
