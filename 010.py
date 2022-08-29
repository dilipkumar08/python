class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        l=len(grid)
        ll=len(grid[0])
        island=0
        for i in range(l):
            for j in range(ll):
                if j+2<ll:
                    if grid[i][j]=="0" and grid[i][j+1]=="1" and grid[i][j+2]=="0":
                        island+=1
                else:
                    break
        return island
        
