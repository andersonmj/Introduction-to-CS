#Checking Sudokus made out of lists to see if they're correct. 

def check_sudoku (p):
  n= len(p)  #size of the grid here!
  digit = 1  #begin in 1.
  while digit<= n: #Go through each digit
    i=0
    while i<n: 
       row_count = 0 
       col_count = 0
       j = 0
       while j<n:  #for each entry in ith column
           if p[i][j]== digit: #check row count 
              row_count = row_count+1
           if p [j][i] == digit:
              col_count == col_count + 1
           j = j+1
      if row_count != 1 or col_count !=1: 
           return False
      i=i+1   #next row/column
   digit = digit +1 #next digit
 return True  #nothing was wrong!
    
