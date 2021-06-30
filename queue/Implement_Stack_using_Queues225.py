class MyStack(object):

    def __init__(self):
        self.array = []

    def push(self, x):
        self.array.append(x)

    def pop(self):
        popint = self.array[-1]
        self.array.pop()
        return popint 

    def top(self):
        return self.array[-1]

    def empty(self):
        if not self.array:
            return True
        else:
            return False
   
   