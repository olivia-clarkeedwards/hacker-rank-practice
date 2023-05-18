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


def getNumberOfSwaps(line, swaps = 0):
    #implement bubble sort 
    # record number of swaps

    for i in range(len(line)):
      value = line[i]
      original_value = i + 1
      if value > original_value + 2:
          print("Too chaotic")
          return
      
    for i in range(len(line) - 1):
        if line[j] > line[j + 1]:
                line[j], line[j + 1] = line[j + 1], line[j]
                swaps += 1
        
        for j in range(len(line) - 1 - i):
            if line[j] > line[j + 1]:
                line[j], line[j + 1] = line[j + 1], line[j]
                swaps += 1

    print(swaps)
    return 
            
        
getNumberOfSwaps([1, 5, 2, 3, 4])      
getNumberOfSwaps([1, 2, 3, 4, 5])
getNumberOfSwaps([1, 2, 5, 3, 4])
getNumberOfSwaps([1, 2, 5, 3, 7, 8, 6, 4])







