import random
c =[]
print("Welcome to Game")
i = 1
for i in range(int(3)):
    print ('input number:' , i)
    b = input()
    b = (int(b))
    c.append(b)
print  (c)

a =[]
a =([random.randint(0, 100) for i in range(3)])
print(a)

#for i in (int(3)): if
if c == a:
    print('congratulate')
else:
    print('Try again!')

#if c == a
 #   print(1)