class MyQueue(object):

    def __init__(self):
        self.array = []
        
    def push(self, x):
        self.array.append(x)
        
    def pop(self):
        popint = self.array[0]
        self.array.pop(0)
        return popint 

    def peek(self):
        return self.array[0]
        
    def empty(self):
        if not self.array:
            return True
        else:
            return False
      