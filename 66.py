
c=[]
#a = 'mnopqrstuvwxy'
a = input("Please input string: ")
# b = input("Please input integer value: ")
# b = (int(b))
# a = a[b:]+a[:b]
# print (a)


#my_string = 'abcdefghijklmno'
my_string = ('abcdefghijklmnopqrstuvwxyz')
my_newstring = (my_string[:len(a)] + a + my_string[len(a):])
#my_string = my_string [:len(a)]
#print(my_string [:len(a)] + a + my_string [len(a):])
i = 0
for i in range(len(a)):
    c.append(my_newstring[i + 1])
#for i in range(len(a)):
    #if a[i] == my_string[i]:
     #   c.append(my_string[i-1])

    #elif a[i] != my_string[i]:
    #    c.append(my_string[i+1])
        #c[i] = my_string[i-1]
#str(c)
m = ''.join(c)
print (m)
#a = [1, 2, 3, 4, 5, 6]
#i = 0
#while i < len(a) - 1:
#    a[i] = a[i + 1]
#    i += 1
#a[i] = 0