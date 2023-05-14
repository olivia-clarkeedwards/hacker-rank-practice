# two players - p1 and p2 
# player 1 moves first, players alternate
# both players move optimally

# n towers of height m
# each player can choose a tower of height x 
# players must reduce height so that the new height is greater than 0 and is a divisor of x.
# that is, 1 <= y < x and x % y = 0
# if a player can't move, they lose the game



def towerBreakers(numTowers, height):
    p1move = True 
    gameOver = False
    winner = None


    towers = [height] * numTowers

    while gameOver is not True:
        currentMoves = [possibleMoves(t) for t in towers]
        print(currentMoves)
        # for i in range(len(numTowers)):
        gameOver = True
            
            
            
        


def possibleMoves(height):
    moves = []
    for i in range(1, height):
        if height % (height - i) == 0:
            moves.append(i)        
    return moves


towerBreakers(2, 6)
    