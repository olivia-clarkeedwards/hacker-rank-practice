class Queue():
    def __init__(self):
        self.stack = []
        
    def enqueue(self, data):
        self.stack.append(data)
                 
    def dequeue(self):
        # if the queue is empty, return 
        # pop off top item and store 
        # if queue is empty, return popped item 
        # add top item back on the stack 
        # return the item returned by the recursive call 

            
        
    def printFrontItem(self):
        if self.size() != 0:
          if not self.isEmpty(self.one):
              for _ in range(len(self.one)):
                  self.two.append(self.one.pop())
          print(self.two[-1])
        else:
            print("Queue empty.")

    def isEmpty(self, stack):
        return stack == []
    
    def size(self):
        return len(self.stack)

        
        

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
        
    
    
    
    
    
       