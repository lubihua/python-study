class Programer:

    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = int(salary)

    def give_raise(self,increase_salary='5000'):
        self.salary += int(increase_salary)