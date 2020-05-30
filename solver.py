class grid:
    def __init__(self,L=None):
        self.L=L
    def is_complete(self):
        for i in range(9):
            for j in range(9):
                if(self.L[i][j] == 0):
                    return False
        return True
    def validationcol(self,j,i):
        H=[]
        if(self.L[i][j]==0):
            return True
        for inter in range(9):
            if(self.L[inter][j] not in H):
                if(self.L[inter][j]!=0):
                    H.append(self.L[inter][j])
            else:
                return False
        return True
    def validationrow(self,i,j):
        if(self.L[i][j]==0):
            return True
        H = []
        for inter in range(9):
            if (self.L[i][inter] not in H):
                if(self.L[i][inter]!=0):
                    H.append(self.L[i][inter])
            else:
                return False
        return True
    def validationsquare(self,i,j):
        rowno=(i//3)*3
        colno=(i//3)*3
        H=[]
        if(self.L[i][j]==0):
            return True
        for ij in range(rowno,rowno+3):
            for ji in range(colno,colno+3):
                if(self.L[ij][ji] not in H):
                    if(self.L[ij][ji]!=0):
                        H.append(self.L[ij][ji])
                else:
                    return False
        return True
    def selfvalidation(self,no):
        J=[0,1,2,3,4,5,6,7,8,9]
        if(int(no) in J):
            return True
        return False
    def validation(self,row,col):
        if(self.validationsquare(row,col) and self.validationrow(row,col) and self.validationcol(col,row) and self.selfvalidation(self.L[row][col])):
            return True
        else:
            return False
    def solve(self,row=0,col=0):
        p=1
        if(row==9 or (row==8 and col==9)):
            return True
        if(col==9 and self.solve(row+1,0)):
            return True
        elif(col==9):
            return False
        if(self.L[row][col]!=0 and col!=8):
            return self.solve(row,col+1)
        elif(self.L[row][col]!=0 and col==8):
            return self.solve(row+1,0)
        while(self.L[row][col]==0 and p<10):
            if(row==9):
                return True
            self.L[row][col]=p
            if(self.validation(row,col)):
                if(col==9 and self.solve(row+1,0)):
                    return True
                jk=self.solve(row,col+1)
                if(jk):
                    return True
                else:
                    self.L[row][col]=0
            else:
                self.L[row][col] = 0
            p+=1
        self.L[row][col]=0
        return False
M=[[0,0,4,6,0,8,9,1,2],
       [6,0,2,1,9,5,3,4,8],
   [1,9,0,3,4,2,5,0,7],
   [8,5,9,7,0,1,4,2,0],
   [0,0,0,0,5,3,7,9,1],
   [7,1,0,9,2,0,8,5,6],
   [0,6,1,5,3,0,2,8,4],
   [0,8,7,0,1,9,0,3,0],
   [0,4,5,0,0,6,1,7,9]]
grid(M)
M=[[8,0,0,0,0,0,0,0,0],
   [0,0,3,6,0,0,0,0,0],
   [0,7,0,0,9,0,2,0,0],
   [0,5,0,0,0,7,0,0,0],
   [0,0,0,0,4,5,7,0,0],
   [0,0,0,1,0,0,0,3,0],
   [0,0,1,0,0,0,0,6,8],
   [0,0,8,5,0,0,0,1,0],
   [0,9,0,0,0,0,4,0,0]]

if __name__=="__main__":
   L=[[0, 0, 0, 7, 3, 0, 5, 4, 9],
      [9, 4, 3, 6, 8, 2, 1, 5, 7],
      [6, 7, 5, 4, 9, 1, 2, 8, 3],
      [2, 5, 4, 3, 6, 7, 8, 9, 1],
      [1, 3, 9, 8, 4, 5, 7, 2, 6],
      [5, 8, 7, 1, 2, 9, 6, 3, 4],
      [7, 2, 1, 9, 5, 4, 3, 6, 8],
      [4, 6, 8, 5, 7, 3, 9, 1, 2],
      [3, 9, 6, 2, 1, 8, 4, 7, 5]] 
   T=grid(L)
   #print(T.L[1][2])
   T.solve()
   print(T.L)
   K=[[8, 1, 2, 7, 3, 6, 5, 4, 9],
 [9, 4, 3, 6, 8, 2, 1, 5, 7],
 [6, 7, 5, 4, 9, 1, 2, 8, 3],
 [2, 5, 4, 3, 6, 7, 8, 9, 1],
 [1, 3, 9, 8, 4, 5, 7, 2, 6],
 [5, 8, 7, 1, 2, 9, 6, 3, 4],
 [7, 2, 1, 9, 5, 4, 3, 6, 8],
 [4, 6, 8, 5, 7, 3, 9, 1, 2],
 [3, 9, 6, 2, 1, 8, 4, 7, 5]]
 #https://www.telegraph.co.uk/news/science/science-news/9359579/Worlds-hardest-sudoku-can-you-crack-it.html
 