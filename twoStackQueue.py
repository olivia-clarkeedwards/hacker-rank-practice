class Queue():
    def __init__(self):
        stack = []

    def enqueue(self, data):
        self.stack.append(data)
    
    def dequeue(self):
        self.stack.pop(0)

    def printFrontItem(self):
        if len(self.stack) != 0:
          print(self.stack[0])
        else:
            print('Queue empty.')
        
        
    

def processQueries():

  queryCount = int(input())
  twoStackQ = Queue()
  for _ in range(queryCount):
      
      q = input().split()

      if q[0] == '1':
          twoStackQ.enqueue(int(q[1]))
      elif q[0] == '2':
          twoStackQ.dequeue()
      else:
          twoStackQ.printFrontItem()

processQueries()
        


    
    
    
       