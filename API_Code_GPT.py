#Write a code to find determinant of a matrix of nxn using recursion

def determinant(matrix): 
    if len(matrix) == 1: 
        return matrix[0][0] 
  
    if len(matrix) == 2: 
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0] 

    det = 0
    for c in range(len(matrix)): 
        det += ((-1)**c)*matrix[0][c]*determinant(getMatrixMinor(matrix, 0, c)) 

    return det 

  
# Function to get the minor of the  
# provided matrix 
def getMatrixMinor(m, i, j): 
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]