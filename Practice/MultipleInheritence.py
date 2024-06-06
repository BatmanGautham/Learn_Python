class Father():
    def F_Parent_method(self):
        print("\nFather : This is from Parent class!\n")

class Mother():
    def M_Parent_method(self):
        print("\nMother : This is from Parent class!\n")

class Kid(Father,Mother):
    def Child_method(self):
        print("\nThis is from Kid class!\n")


obj1 = Father()
obj2 = Mother()
obj3 = Kid()


obj1.F_Parent_method()
obj2.M_Parent_method()
obj3.Child_method()

obj3.F_Parent_method()
obj3.M_Parent_method()