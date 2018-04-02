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
    def __init__(self, name, job=None, pay=0, exp=0, effcoeff=0, workingpeople=0, man=None):
        self.name = name
        self.job = job
        self.pay = pay
        self.exp = exp
        self.effcoeff = effcoeff
        self.workingpeple = workingpeople
        self.man = man


    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))

    def __str__(self):
        return '[Person: %s, job: %s, salary: %s, experience= %s, manager: %s]' % (self.name,  self.job, self.pay, self.exp, self.man)

    def exper(self):
        if 2 <= self.exp < 5:
           self.pay = self.pay + 200
        elif self.exp >= 5:
            self.pay = self.pay * 1.2 + 500
        return self.pay

    def salary(self):
        print('[Person: %s got salary: %s$]' % (self.name, self.pay))



class Dev(Person):
     def __init__(self, name, pay, exp, man ):
         Person.__init__(self, name, 'Dev', pay, exp, man)



class Design(Person):
     def __init__(self, name, pay, exp, effcoeff, man):
         Person.__init__(self, name, 'Des', pay, exp, effcoeff, man)

     def giveRaise(self, percent, bonus=100):
         Person.giveRaise(self, percent + bonus)

     def salary(self):
         self.pay = self.pay * self.effcoeff
         print('[Designer: %s got salary: %s$]' % (self.name, self.pay))

class Manager(Person):
    def __init__(self, name, pay, workingpeple, exp):
        Person.__init__(self, name, 'mgr', pay, workingpeple, exp)

    def giveRaise(self, percent, bonus=100):
        Person.giveRaise(self, percent + bonus)

    def salary(self):
        if self.workingpeple >= 5:
           self.pay = self.pay + 200
        elif self.exp >= 10:
            self.pay = self.pay + 300
        print('[Manager: %s got salary: %s$]' % (self.name, self.pay))

ivan = Dev('Ivan Petrov',pay=4, exp=3, man='Vasya')
john = Design('John Sidorov', pay=250, exp=2, effcoeff=10, man ='Petya')
Petr = Manager('Mysha Pupkin', pay=100, workingpeple=16, exp=5)
print(ivan)
print(john)
ivan.exper()
john.exper()
Petr.exper()
ivan.salary()
john.salary()
Petr.salary()
print(ivan)
print(john)
print(Petr)
# print(john)
# john.giveRaise(.10)
# print(john)
# tom = Manager('Tom Jones', 30000)
# tom.giveRaise(.10)
# print(tom)

