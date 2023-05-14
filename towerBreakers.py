# two players - p1 and p2 
# player 1 moves first, players alternate
# both players move optimally

# n towers of height m
# each player can choose a tower of height x 
# players must reduce height so that the new height is greater than 0 and is a divisor of x.
# that is, 1 <= y < x and x % y = 0
# if a player can't move, they lose the game


# FUNCTION RETURNS WINNING PLAYER (INT)



def towerBreakers(numTowers, height):
    
    if height == 1:
        return 2
    
    return int(numTowers % 2 == 0) + 1
    

    