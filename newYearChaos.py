'''

Description: Counts the minimum amount of swaps needed to reach the given list from a sorted list in ascending order. If any element is more than two swaps from its original position, prints "Too chaotic".Else, prints minimum number of swaps required. 
Author: Olivia Clarke-Edwards

'''
 
def minimumBribes(line):
    n = len(line)

    for i in range(n):
        if line[i] > i + 3:
            print('Too chaotic')
            return 
        
    print(getNumberOfSwaps(line))
    return

def getNumberOfSwaps(line, swaps = 0, memo = {}):
    n = len(line)
    key = ','.join([str(num) for num in line])
    sorted = True
    if key in memo:
        return memo[key]
    
    for i in range(n - 1):
        if line[i] > line[i + 1]:
            line[i], line[i + 1] = line[i + 1], line[i]
            swaps += 1
            sorted = False

    if sorted:
        return swaps
    else:
        memo[key] = getNumberOfSwaps(line[:n], swaps, memo)
        return memo[key]
             
minimumBribes([1, 5, 2, 3, 4])
minimumBribes([1, 2, 3, 4, 5])     
minimumBribes([1, 2, 5, 3, 4])     
minimumBribes([1, 2, 5, 3, 7, 8, 6, 4])        










