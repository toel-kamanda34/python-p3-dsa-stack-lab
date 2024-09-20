class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit
        

    def isEmpty(self):
        return len(self.items) ==  0 #if list is empty return true

   #add a new item to the top of the stack
    def push(self, item):
        if len(self.items) < self.limit:
            self.items.append(item)
        else:
            print("Stack is full")
    #last in first out
    def pop(self):
        if self.isEmpty():
            return None
        return self.items.pop()

    #return top element without removing it 
    def peek(self):
        if self.isEmpty():
            return None
        return self.itmes[-1]
    
    #return length of items list
    def size(self):
        return len(self.items)

    #check if the stack has reached our limit
    def full(self):
        return len(self.items) >= self.limit

    #looks for an iten and returns how far it is from the top if not foun return -1 
    def search(self, target):
        if target in self.items:
            return len(self.items) - self.items.index(target) - 1
        return -1


my_stack = Stack([1, 2, 3], limit=5)
print(my_stack.isEmpty())  
my_stack.push(4)
my_stack.push(5)
my_stack.push(6)  
