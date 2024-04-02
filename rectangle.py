class sum:
    def _init_(self,length,breadth):
        self.length = length
        self.breadth = breadth

        
    def mul(self):
        print("Area is ",self.length * self.breadth)



obj = sum()
obj._init_(4,2)
obj.add()