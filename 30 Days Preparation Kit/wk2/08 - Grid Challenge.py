# https://www.hackerrank.com/challenges/one-month-preparation-kit-grid-challenge/problem
def gridChallenge(grid):
    
    grid = [sorted(g) for g in grid]
        
    for col in range(len(grid[0])):
        rows = [grid[row][col] for row in range(len(grid))]
        if rows != sorted(rows):
            return 'NO'
    return 'YES'
