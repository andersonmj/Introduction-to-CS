# A list is symmetric if the first row is the same as the first column,
# the second row is the same as the second column and so on. Write a
# procedure, symmetric, which takes a list as input, and returns the
# boolean True if the list is symmetric and False if it is not.

def symmetric (m):  #assuming it's a normal matrix and not []. If it's [] add if m:  ... else return True.
    if len (m) == len (m[0]): #check if its nxn
        i = 0 #choosing row and column 
        while i<len(m): #go from number to number without exceeding the limit
        j=0 #extra counter. 
            while j < len (m): #limits!
                if m[i][j] == m [j][i]: #comparing
                    j=j+1
                else: 
                    return False #in case they're not equal
            i=i+1
        return True    
    else: 
        return False    
    
# Test cases: 

print symmetric([[1, 2, 3],
                [2, 3, 4],
                [3, 4, 1]])
#>>> True

print symmetric([["cat", "dog", "fish"],
                ["dog", "dog", "fish"],
                ["fish", "fish", "cat"]])
#>>> True

print symmetric([["cat", "dog", "fish"],
                ["dog", "dog", "dog"],
                ["fish","fish","cat"]])
#>>> False


print symmetric([[1, 2],
                [2, 1]])
#>>> True


print symmetric([[1, 2, 3, 4],
                [2, 3, 4, 5],
                [3, 4, 5, 6]])
#>>> False


print symmetric([[1,2,3],
                 [2,3,1]])
#>>> False
