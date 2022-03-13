import numpy as np
grid=[[0,7,2,0,0,9,0,0,0],
      [0,3,0,6,0,0,4,0,0],
      [0,0,1,0,0,0,0,8,7],
      [1,0,0,0,0,0,7,0,0],
      [9,0,0,2,0,3,0,0,0],
      [0,0,0,0,0,0,0,0,0],
      [0,0,0,3,0,0,5,6,0],
      [0,0,0,0,0,4,9,0,0],
      [0,0,0,0,1,8,0,0,0]]
def possible(y,x,n):
    for i in range(0,9):
        if n == grid[i][x]:
            return False
    for i in range(0,9):
        if n== grid[y][i]:
            return False
    x0=(x//3)*3
    y0=(y//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if grid[y0+i][x0+j]==n:
                return False
    return True
def check():
    for i in range(9):
        for j in range(9):
            if grid[i][j]==0:
                return False
    return True
def solve():
    
    for i in range(9):
        for j in range(9):
            if grid [i][j]==0:
                for a in range(1,10):
                    if possible(i,j,a):
                        grid [i][j] = a
                        a=solve()
                        if check()==False:
                            grid [i][j] = 0
                return
    
     
          
    
      

                       

solve()
print(grid)



