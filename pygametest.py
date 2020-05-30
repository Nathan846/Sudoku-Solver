import pygame
from datetime import datetime
from solver import grid
def text_objects(Text,font):
    TextSurface=font.render(Text,0,WHITE)
    return TextSurface,TextSurface.get_rect()
def cleartext(Text,font):
    TextSurface=font.render(Text,0,BLACK)
    return TextSurface,TextSurface.get_rect()
def drawGrid(surface):
    blocksize = 50 #Set the size of the grid block
    for x in range(75,WINDOW_WIDTH-75,blocksize):
        for y in range(50,WINDOW_HEIGHT-100,blocksize):
            rect = pygame.Rect(x, y,blocksize, blocksize)
            #rect(left,top,width,height) creates a rectangle of coordinates (left,top) with width and height
            pygame.draw.rect(t, WHITE, rect, 1)#Realize the rectangle
    GRIDSTARTLEFT=75
    GRIDENDLEFT=525
    GRIDSTARTTOP=50
    GRIDENDTOP=500
    for i in range(1,3):
        h=3*i*blocksize
        pygame.draw.line(surface,WHITE,(75+h,50),(75+h,500),10)
        pygame.draw.line(surface,WHITE,(75,50+h),(525,h+50),10)
    string="Sudoko Solver"
    font=pygame.font.Font('Arial.ttf', 32)  
    textSurf, textRect=text_objects(string,font)
    textRect.center = (300, 37)
    surface.blit(textSurf,textRect)
def managetime(surface):
    string=""
    font=pygame.font.Font('Arial.ttf', 30)
    surface.fill(BLACK, (0, 500, 600, 100))
    nowtime=datetime.now()-starttime
    string="Time:"+str(nowtime).split(".")[0]
    textSurf, textRect=text_objects(string,font)
    textRect.center= (460,550)
    surface.blit(textSurf,textRect)
    return nowtime
class highlighter:
    def __init__(self,surface,ls):
        self.blocksize=50
        self.i=75
        self.j=50
        self.rt=pygame.Rect(self.i,self.j,self.blocksize,self.blocksize)
        pygame.draw.rect(surface,GREEN,self.rt,5)
        self.lockedelements(ls)
        self.initial(ls,surface)
        
    def change(self,surface,i,j):
        pygame.draw.rect(surface,BLACK,self.rt,5)
        self.rt=pygame.Rect(i,j,self.blocksize,self.blocksize)
        pygame.draw.rect(surface,GREEN,self.rt,5)
    def right(self,surface):
        self.i+=50
        if(self.i>475):
            self.i=475
        self.change(surface,self.i,self.j)
    def left(self,surface):
        self.i-=50
        if(self.i<75):
            self.i=75
        self.change(surface,self.i,self.j)
    def up(self,surface):
        self.j-=50
        if(self.j<50):
            self.j=50
        self.change(surface,self.i,self.j)
    def down(self,surface):
        self.j+=50
        if(self.j>450):
            self.j=450
        self.change(surface,self.i,self.j)
        
    def initial(self,ls,surface):
        for i in range(9):
            for j in range(9):
                row=100+(50*i)
                col=75+(50*j)
                if(ls[i][j]!=0 and (i,j) in self.G):
                    self.numberalign(surface,row,col,str(ls[i][j]))  
    def detectzero(self,t,ls):
        for i in range(9):
            for j in range(9):
                row=75+(50*i)
                col=50+(50*j)
                if(ls[i][j] == 0):
                    t.fill(BLACK, (row, col, self.blocksize, self.blocksize))        
    def complete(self,surface,string):
        font=pygame.font.Font('Arial.ttf', 30)
        k=str(string).split(".")[0]
        surface.fill((0,0,0), (0, 510, 600, 100))        
        strsd = "You have completed this puzzle in "+k
        textSurf, textRect=text_objects(strsd,font)
        textRect.center = (300,550)        
        surface.blit(textSurf,textRect)
        pygame.display.update()
        

    def numberalign(self,surface,row,col,string):
        font=pygame.font.Font('Arial.ttf', 30)
        textSurf, textRect=text_objects(string,font)
        textRect.center= (row,col)
        surface.blit(textSurf,textRect)
    def lockedelements(self,ls):
        self.G = []
        for i in range(9):
            for j in range(9):
                if(ls[i][j]!=0):
                    self.G.append((i,j))  
    def enter(self,surface,string,Grid):
        row = (self.i-75)//50
        col = (self.j - 50)//50
        if((row,col) in self.G):
            print(row,col)
            print('locked')
            return
        Grid.L[row][col] = int(string)
        #print(Grid.L)
        #print(row,col,Grid.L[row][col])
        if(Grid.validation(col,row)):
            font=pygame.font.Font('Arial.ttf', 20)
            textSurf, textRect=text_objects(string,font)
            textRect.center= (self.i+10,self.j+15)
            surface.blit(textSurf,textRect)
            return
        Grid.L[row][col] = 0
        return
    def delete(self,surface,Grid):
        row = (self.i-75)//50
        col = (self.j - 50)//50
        if((row,col) in self.G):
            print('locked')
            return
        surface.fill(BLACK, (self.i, self.j, self.blocksize, self.blocksize))
        print(row,col,Grid.L[row][col])
        Grid.L[row][col]=0
        print(Grid.L)
        return
pygame.init()
t=pygame.display.set_mode((600,600))
running=True
starttime=datetime.now()
M=[[0,0,4,6,0,8,9,1,2],
   [6,0,2,1,9,5,3,4,8],
   [1,9,0,3,4,2,5,0,7],
   [8,5,9,7,0,1,4,2,0],
   [0,0,0,0,5,3,7,9,1],
   [7,1,0,9,2,0,8,5,6],
   [0,6,1,5,3,0,2,8,4],
   [0,8,7,0,1,9,0,3,0],
   [0,4,5,0,0,6,1,7,9]]
Grid=grid(M)
GREEN = (0,200,0)
BLACK = (0,0,0)
WHITE = (200,200,200)
t.fill(BLACK)
WINDOW_WIDTH = 600
WINDOW_HEIGHT= 600
ht=highlighter(t,Grid.L)
jk=1
while(running and jk):    
    drawGrid(t)
    gsd=datetime.now()-starttime
    if(Grid.is_complete()):
        ht.complete(t,str(gsd))
        break
    for event in pygame.event.get():
        if(event.type==pygame.QUIT):#When we click the red X button, the window closes
            running=False
        if(event.type==pygame.KEYDOWN):
            if(event.key==pygame.K_RIGHT):
                ht.right(t)
            if(event.key==pygame.K_LEFT):
                ht.left(t)
            if(event.key==pygame.K_UP):
                ht.up(t)
            if(event.key==pygame.K_DOWN):
                ht.down(t)
            if(event.key==pygame.K_SPACE):
                Grid.solve()
                j=highlighter(t,Grid.L)
                jk=0
                break
            if(event.key==pygame.K_1):
                ht.enter(t,str(1),Grid)
            if(event.key == pygame.K_2):
                ht.enter(t,str(2),Grid)
            if(event.key == pygame.K_3):
                ht.enter(t,str(3),Grid)
            if(event.key == pygame.K_4):
                ht.enter(t,str(4),Grid)
            if(event.key == pygame.K_5):
                ht.enter(t,str(5),Grid)
            if(event.key == pygame.K_6):
                ht.enter(t,str(6),Grid)
            if(event.key == pygame.K_7):
                ht.enter(t,str(7),Grid)
            if(event.key == pygame.K_8):
                ht.enter(t,str(8),Grid)
            if(event.key == pygame.K_9):
                ht.enter(t,str(9),Grid)
            if(event.key == pygame.K_BACKSPACE or event.key == pygame.K_DELETE):
                ht.delete(t,Grid)
    gh=managetime(t)
    pygame.display.update()
running=True
while(running):
    for event in pygame.event.get():
        if(event.type==pygame.QUIT):#When we click the red X button, the window closes
            running=False    
    
    
