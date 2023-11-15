class CircularQueue:

    def __init__(self, size):
        self.size = size
        self.queue = [None for i in range(size)] 
        self.front = self.rear = -1

    def Isempty(self):
        if self.front == -1:
            return True
        
    def Isfull(self):
        if ((self.front == 0 and self.rear == -1) or ((self.rear+1) % self.size == self.front )):
            return True

    def Peek(self):
        return self.queue[self.front]

    def Enqueue(self, val):
        if self.Isfull():
            return False
        
        elif self.Isempty():
            self.front = self.rear = 0
            self.queue[self.rear] = val

        # one round is complete
        else:
            self.rear = (self.rear + 1) % self.size 
            self.queue[self.rear] = val

    def Dequeue(self): # remove from queue
        if self.Isempty()==True:
            print("The queue is empty!")
            return
        else:
            temp = self.queue[self.front]
            self.queue[self.front] = None
            self.front = (self.front + 1) % self.size
            return temp
   
    def Reverse(self): 
        start = self.front
        end = self.rear
        A = self.queue
        while start < end: 
            A[start], A[end] = A[end], A[start] 
            start += 1
            end -= 1

            
