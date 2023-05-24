class Queue():
    def __init__(self):
        self.stack = []
        
    def enqueue(self, data):
        self.stack.append(data)
                 
    def dequeue(self):
        # if the queue is empty, return 
        if self.size() <= 0:
            return 
        
        top_item = self.stack.pop()

        if self.size() == 0:
            return top_item
        
        front_item = self.dequeue()

        self.stack.append(top_item)

        return front_item

            
        # pop off top item and store 
        # if queue is empty, return popped item 
        # add top item back on the stack 
        # return the item returned by the recursive call 

            
        
    def printFrontItem(self):

        # if the queue is empty, return 
        if self.size() <= 0:
            return
        
        top_item = self.stack.pop()

        if self.size() == 0:
            print(top_item) 
        
        self.printFrontItem()
        self.stack.append(top_item)
    
        

    def isEmpty(self, stack):
        return stack == []
    
    def size(self):
        return len(self.stack)
    
    def toString(self):
        return self.stack

        
        

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
        


    
    
    
       