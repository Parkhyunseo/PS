N=int(input())

class Queue(object):
    def __init__(self):
        self.queue=[]
        self.result=[]
        
    def push(self, x):
        self.queue.append(x)
        
    def pop(self):
        if len(self.queue)==0:
            x = -1
        else:
            x = self.queue.pop(0)
        self.result.append(x)
    
    def size(self):
        self.result.append(len(self.queue))
        
    def empty(self):
        self.result.append( 1 if len(self.queue) is 0 else 0)
    
    def front(self):
        if len(self.queue) == 0:
            self.result.append(-1)
        else:
            self.result.append(self.queue[0])
    
    def back(self):
        if len(self.queue) == 0:
            self.result.append(-1)
        else:
            self.result.append(self.queue[-1])
        
    def get_result(self):
        return self.result
    
s = Queue()

for _ in range(N):
    inst = input().split()
    if len(inst) >= 2:
        getattr(s, inst[0])(inst[1])
    else:
        getattr(s, inst[0])()
        
for i in s.get_result():
    print(i)