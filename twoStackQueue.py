class Queue():
    def __init__(self):
        self.input = []
        self.output = []
        
    def enqueue(self, data):
        if len(self.output) == 0:
            self.input.append(data)
        else:
            while len(self.output) > 0:
                self.input.append(self.output.pop())
            self.input.append(data)

    def dequeue(self):
        
        if len(self.input) != 0:
            while len(self.input) != 0:
              self.output.append(self.input.pop()) 

        if len(self.output) != 0:
          self.output.pop()
        
    def printFrontItem(self):
        
        if len(self.input) == 0 and len(self.output) == 0:
            print('Queue is empty.')
        else:
            if len(self.input) != 0:
                print(self.input[0])
            else:
                print(self.output[-1])

    

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
        


    
    
    
       