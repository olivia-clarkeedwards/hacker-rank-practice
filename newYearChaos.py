# take a list that contains mixed integers 1 to n where n is the size of the list 
# if the value of a number in the list is more than two places away from its index + 1, return "too much chaos"
# else if the value is greater than its index, add (value - 1) - current_index

# def getNumberOfSwaps(line):
#     bribes = 0
    
#     for index in range(len(line)):
#         value = line[index]
#         original_value = index + 1
#         if value > original_value + 2:
#             print("Too chaotic")
#             return
#         elif value > original_value:
#             bribes += value - original_value
            
          
    
#     print(bribes)
#     return 



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
            


        
print(getNumberOfSwaps([1, 5, 2, 3, 4]))
print(getNumberOfSwaps([1, 2, 3, 4, 5]))     
print(getNumberOfSwaps([1, 2, 5, 3, 4]))     
print(getNumberOfSwaps([1, 2, 5, 3, 7, 8, 6, 4]))        










