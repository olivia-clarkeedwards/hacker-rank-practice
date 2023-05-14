'''
Description: Given a set A, apply updates and sets specified. Return resulting sum of set A. 
Solution by Olivia Clarke-Edwards 
Problem: https://www.hackerrank.com/challenges/py-set-mutations/problem
'''

# Sample input:

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

# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys 

def performOperation(setA, setB, op):
  if op == 'update':
    setA.update(setB)
  elif op == 'intersection_update':
    setA.intersection_update(setB)
  elif op == 'symmetric_difference_update':
    setA.symmetric_difference_update(setB)
  elif op == 'difference_update':
    setA.difference_update(setB)
    

def main():

  input()
  setA = set([int(num) for num in input().split()])
  numofOtherSets = int(input().strip())

  for index in range(numofOtherSets):
    operation = input().split()[0]
    setB = set([int(num) for num in input().split()])
    performOperation(setA, setB, operation)
        

  print(sum(setA))
    
main()
