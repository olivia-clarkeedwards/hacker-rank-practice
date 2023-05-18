# Enter your code here. Read input from STDIN. Print output to STDOUT

class Queue():
    def __init__(self):
        self.one = []
        self.two = []
        
    def enqueue(self, data):
        if not self.isEmpty(self.two):
            for _ in range(len(self.two)):
                self.one.append(self.two.pop())
        self.one.append(data)
                 
    def dequeue(self):
        if self.size() != 0:
          if not self.isEmpty(self.one):
              for _ in range(len(self.one)):
                  self.two.append(self.one.pop())
          self.two.pop()
        else:
             print("Cannot dequeue, queue is empty.")
            
        
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
        return len(self.one + self.two)

        
        

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
        
    
    
    
    
    
       