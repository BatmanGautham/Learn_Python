class sum:
    def read(self):
        self.x = int(input("Enter first number : "))
        self.y = int(input("Enter second number : "))
    
    def add(self):
        print("Sum is ",self.x + self.y)



obj = sum()
obj.read()
obj.add()