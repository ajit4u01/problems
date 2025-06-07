#User function Template for python3

class Solution:
    
    #Function to search a given integer in a matrix.
    def searchMatrix(self,matrix, x): 
    	# code here 
        for row in matrix:
            for val in row:
                if val == x:
                    return True
        return False