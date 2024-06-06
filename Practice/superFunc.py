class Company:
    def company_name(self):
        return 'Coconut'
    
class Employee(Company):
    def mess(self):
        c_name = super().company_name()
        print("We work in ",c_name)

obj = Employee()
obj.mess()