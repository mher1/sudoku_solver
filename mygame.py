import pygame
from copy import deepcopy
from sys import exit
grid=[[0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0]]

grid_original = [[grid[x][y] for y in range(len(grid[0]))] for x in range(len(grid))]
buffer = 10
background_color="GRAY65"

def insert(win, position):
    i,j = position[0], position[1]
  
    myfont = pygame.font.SysFont('arial', 34)
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if possible(j,i,event.key-48):
                    if(grid_original[i-1][j-1] != 0):
                        return
                    
                    if(event.key == 48): #checking with 0
                        grid[j][i] = event.key - 48
                        pygame.draw.rect(win, background_color, (position[0]*50 + buffer, position[1]*50+ buffer,50 -2*buffer , 50 - 2*buffer))
                        pygame.display.update()
                        return
                    if(0 < event.key - 48 <10):  #We are checking for valid input
                        pygame.draw.rect(win, background_color, (position[0]*50 + buffer+1, position[1]*50+ buffer,50 -2*buffer , 50 - 2*buffer))
                        value = myfont.render(str(event.key-48), True, "red")
                        
                        
                        win.blit(value, (position[0]*50 +18, position[1]*50+5))
                        grid[j][i] = event.key - 48
                        pygame.display.update()
                        return
                return

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
                
def main():

    pygame.init() 
    screen  =  pygame.display.set_mode((550,600))
    pygame.display.set_caption("sudoku solver!!")
    clock = pygame.time.Clock()
    main_surface=pygame.Surface(((450,450)))
    main_surface.fill("GRAY65")
    my_font=pygame.font.SysFont("arial",36)
    screen.fill("GRAY85")
    original_grid_element_color = (52, 31, 151)
   
    pygame.draw.rect(screen,"gray25",(150,525,252,50))
    rect=pygame.draw.rect(screen,"gray85",(155,530,242,40))


            
    

    img = my_font.render('solve!!', True,"black")
    screen.blit(img, (235,525))
    
    for i in range(0,10):
        if i%3==0:
            

            pygame.draw.line(main_surface,("black"),(49.8*i,0),(49.8*i,450),4)
            pygame.draw.line(main_surface,("black"),(0,49.8*i),(450,49.8*i),4)
        else:
            pygame.draw.line(main_surface,("black"),(50*i,0),(50*i,450),2)
            pygame.draw.line(main_surface,("black"),(0,50*i),(450,50*i),2)
        
    pygame.display.update()
    for i in range(0, len(grid[0])):
        for j in range(0, len(grid[0])):
            if(0<grid[i][j]<10):
                value = my_font.render(str(grid[i][j]), True, original_grid_element_color)
                main_surface.blit(value, ((j)*50+18 , (i)*50 +5))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                
                insert(main_surface, ((pos[0]//50)-1, (pos[1]//50)-1))
            if event.type== pygame.MOUSEBUTTONDOWN:
                if rect.collidepoint(pos):
                    grid_copy=deepcopy(grid)
                    solve()
                    for j in range(0, len(grid_copy)):
                        for i in range(0, len(grid_copy[j])):
                            if grid_copy[j][i]!=0:
                                grid[j][i]=0

                            
                    
                    for i in range(0, len(grid[0])):
                        for j in range(0, len(grid[0])):
                            if(0<grid[i][j]<10):
                                value = my_font.render(str(grid[i][j]), True, original_grid_element_color)
                                main_surface.blit(value, ((j)*50+18 , (i)*50 +5))
                    pygame.display.update()
                    
            

            if event.type==pygame.QUIT:
                pygame.quit()
                exit()
        screen.blit(main_surface,(50,50))
    



        pygame.display.update()
        clock.tick(50)


main()
