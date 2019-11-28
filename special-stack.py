class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self, x):
         return x == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

class SpecialStack(Stack):
    def __init__(self):
        self.items = []
        self.minItem = []
        
        
    def push(self, item):
        if(super().isEmpty(self.items)):
            super().push(item)
            self.minItem.append(item)
        else:
            super().push(item)
            y = self.minItem.pop()
            self.minItem.append(y)
            if(item < y):
                self.minItem.append(item)
            else:
                self.minItem.append(y)

    def pop(self):
        x = super().pop()
        self.minItem.pop()
        return x
	
    def getMin(self):
        x = self.minItem.pop()
        self.minItem.append(x)
        return x


s = SpecialStack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
print(s.getMin())
s.push(5)
print(s.getMin())
            
        
        