def ADD_MAT(x,y):
   for i <- 0 to length(x): #rows
    for j <- 0 to length(x[0]): #columns
        add[i][j] <- x[i][j] + y[i][j]
   for a in add:
      print(a)
   
def SUB_MAT(x,y):
   for i <- 0 to length(x):
    for j <- 0 to length(x[0]):
        sub[i][j] <- x[i][j] - y[i][j]
   for s in sub:
      print(s)
   
def MULT_MAT(x,y):
   for i <- 0 to length(x):
    for j <- 0 to length(y[0]): #y columns
        for k <- 0 to length(y): #y rows
            mult[i][j] <- x[i][j] * y[i][j]
   for m in mult:
      print(m)

      
A <- B*C –2*(B+C)
A1 <- MULT_MAT(B,C)
A2 <- ADD_MAT(B,C)
A3 <- MULT_MAT (A2,2)
A <- A1 - A3
