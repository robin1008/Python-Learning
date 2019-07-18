grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

for x in range(6):
    for y in range(9):
        print(grid[y][x], end='')
    print('\n')

'''
print(len(grid[0]))
print(len(grid))
for n in range(len(grid[0])):
 for m in range(len(grid)):
  print(grid[m][n], end='')
 print('\n')
'''