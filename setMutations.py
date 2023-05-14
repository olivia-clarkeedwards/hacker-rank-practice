
# 16 - number of elements in set A 
# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 24 52 - elements in set A 
# 4 - number of other sets 
# intersection_update 10 - operation, number of operations in next set 
# 2 3 5 6 8 9 1 4 7 11         
# update 2 - operation, number of operations in next set 
# 55 66
# symmetric_difference_update 5 - operation, number of operations in next set 
# 22 7 35 62 58
# difference_update 7 - operation, number of operations in next set 
# 11 22 35 55 58 62 66

import sys 

def main():

  # create an array of inputs
  count = 0
  setA = set()
  setB = set()
  numofOtherSets = 0
  while count < 3:
    for line in sys.stdin:
      if count == 1:
        setA = set([int(num) for num in line.split()])
      elif count == 2:
        numofOtherSets = int(line.strip())
      count += 1 
      break

  count = 0
  while count < numofOtherSets:
    for op in sys.stdin:
      operation = op.split()[0]
      for nextSet in sys.stdin:
        setB = set([int(num) for num in nextSet.split()])
        performOperation(setA, setB, operation)
        break
      count += 1
      break

  return sum(setA)


def performOperation(setA, setB, op):
  print(setA, setB)
  if op == 'update':
    setA.update(setB)
  elif op == 'intersection_update':
    setA.intersection_update(setB)
  elif op == 'symmetric_difference_update':
    setA.symmetric_difference_update(setB)
  elif op == 'difference_update':
    setA.difference_update(setB)



    

main()