def gridChallenge(grid):
    arrGrid = [sorted([*s]) for s in grid]
    [s.sort() for s in arrGrid]
    numOfColumns = len(arrGrid[0])

    for col in range(numOfColumns):
        column = [row[col] for row in arrGrid]
        sorted_column = sorted(column)
        if not column == sorted_column:
            return 'NO'
        
    return 'YES'

print(gridChallenge(['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv']))