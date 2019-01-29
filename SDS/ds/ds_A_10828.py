N=int(input())

class Stack(object):
    def __init__(self):
        self.stack=[]
        self.result=[]
        
    def push(self, x):
        self.stack.append(x)
        
    def pop(self):
        if len(self.stack)==0:
            x = -1
        else:
            x = self.stack.pop()
        self.result.append(x)
    
    def size(self):
        self.result.append(len(self.stack))
        
    def empty(self):
        self.result.append( 1 if len(self.stack) is 0 else 0)
    
    def top(self):
        if len(self.stack) == 0:
            x = -1
        else:
            x=self.stack.pop()
            self.stack.append(x)
        self.result.append(x)
        
    def get_result(self):
        return self.result
    
s = Stack()

for _ in range(N):
    inst = input().split()
    if len(inst) >= 2:
        getattr(s, inst[0])(inst[1])
    else:
        getattr(s, inst[0])()
        
for i in s.get_result():
    print(i)