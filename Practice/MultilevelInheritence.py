class Father():
    def Parent_method(self):
        print("\nFather : This is from Parent class!\n")

class Child(Father):
    def Child1_method(self):
        print("\nThis is from Child class!\n")

class GrandChild(Child):
    def Child2_method(self):
        print("\nThis is from grandchilds class!\n")


obj1 = Father()
obj2 = Child()
obj3 = GrandChild()


obj1.Parent_method()
obj2.Child1_method()
obj3.Child2_method()

obj2.Parent_method()

obj3.Parent_method()
obj3.Child1_method()