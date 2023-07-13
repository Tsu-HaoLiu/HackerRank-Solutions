


def flippingMatrix(matrix):
    
    n = len(matrix) //2
    total = 0
    
    for row in range(n):
        for col in range(n):
            top_left = matrix[row][col]
            top_right = matrix[row][2*n-col-1]
            bottom_left = matrix[2*n-row-1][col]
            bottom_right = matrix[2*n-row-1][2*n-col-1]
            
            total += max(top_left, top_right, bottom_left, bottom_right)
    
    return total