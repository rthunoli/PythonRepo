
class Employee:
    num_of_emps = 0
    raise_amount = 1.04

    # def __setattr__(self, name, value):
    #     if name in ['first', 'last', 'email', 'pay']:
    #         super().__setattr__(name,value)

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + "." + last + "@gmail.com"
        self.pay = pay
        Employee.num_of_emps += 1

    def __del__(self):
        Employee.num_of_emps -= 1

    @classmethod
    def from_string(cls, emp_string):
        first, last, pay = emp_string.split('-')
        return cls(first, last, pay)

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

emp1 = Employee("Rajendran","Thunoli",50000)
emp1.doj = "2014-10-26"
print(str(emp1))
#print("hello")

# print(emp1.__dict__)
# del emp1.doj
# print(emp1.__dict__)
# print(Employee.num_of_emps)
# del emp1
# print(Employee.num_of_emps)


#emp2 = Employee("Test","User",60000)

# s1 = "Rajendran-Thunoli-50000"
# s2 = "Test-User-60000"
# emp1 = Employee.from_string(s1)
# emp2 = Employee.from_string(s2)
# print(emp1.email)
# print(emp2.email)
# print(emp1.num_of_emps)
