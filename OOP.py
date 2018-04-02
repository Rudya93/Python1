# There are 3 types of employee: developer, designer and manager
# Each employee has: first name, second name, salary, experiance (years) and manager
# Each designer has effectivness coefficient(0-1)
# Each manager has team of developers and designers.
# Department should have list of managers(which have their own teams)
# Department should be able to give salary (for each employee message: "@firstName@ @secondName@: got salary: @salaryValue@")
# Each employee gets the salary, defined in field Salary. If experiance of employee is > 2 years, he gets bonus + 200$, if experiance is > 5 years, he gets salary*1.2 + bonus 500
# Each designer gets the salary = salary*effCoeff
# Each manager gets salary +
#
#
# 200$ if his team has >5 members
# 300$ if his team has >10 members
# salary*1.1 if more than half of team members are developers.
#
#
# Redefine string representation for employee as follows: "@firstName@ @secondName@, manager:@manager secondName@, experiance:@experiance@"
#
#
class Person:
    def __init__(self, name, job=None, pay=0, exp=0, man=None):
        self.name = name
        self.job = job
        self.pay = pay
        self.exp = exp
        self.man = man


    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))

    def __str__(self):
        return '[Person: %s, job: %s, salary: %s, manager: %s]' % (self.name,  self.job, self.pay, self.man)

    def exper(self):
        if 2 <= self.exp < 5:
            self.pay = self.pay + 200
        elif self.exp >= 5:
            self.pay = self.pay * 1.2 + 500



class Dev(Person):
     def __init__(self, name, pay):
         Person.__init__(self, name, 'Dev', pay)



class Design(Person):
     def __init__(self, name, pay):
         Person.__init__(self, name, 'Des', pay)

     def giveRaise(self, percent, bonus=100):
         Person.giveRaise(self, percent + bonus)


class Manager(Person):
    def __init__(self, name, pay):
        Person.__init__(self, name, 'mgr', pay)

    def giveRaise(self, percent, bonus=100):
        Person.giveRaise(self, percent + bonus)

ivan = Person('Ivan Petrov', job='dev', pay=4, exp=3, man='Vasya')
john = Person('John Sidorov', job='dev', pay=60000, exp=2, man ='Petya')
Petr = Person('Mysha Pupkin', job ='mgr', pay=100, exp=5)
print(ivan)
ivan.exper()
print(ivan)
print(john)
print(Petr)
# print(john)
# john.giveRaise(.10)
# print(john)
# tom = Manager('Tom Jones', 30000)
# tom.giveRaise(.10)
# print(tom)

