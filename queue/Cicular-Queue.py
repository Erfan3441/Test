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

    

            
