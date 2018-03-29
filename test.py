a = 'ZENOVW'
b = sorted(a)
print (b)
#['E', 'N', 'O', 'V', 'W', 'Z']
c = ''.join(b)
print (c)



import string
#print (string.ascii_uppercase)
for c in string.ascii_letters:
    print(c)

s = 'fooУБРАТЬbarОТСЮДАbazНЕЛАТИНСКОЕ'
s2 = ''.join(c for c in s if c in string.ascii_letters)
print(s2)
#chr(65)
#'A'
#chr(122)
#'z'
#print(chr(128522))





#a = []
#i=0
#for i in range(int(3)):
#    b = input("input matrix 1: ")
#    a.append(b)
#print (a)
#num_array[:, i]

  #a = [1, 2, 3]
  #print (a[: 3])
#num_array = list()
#num = input("Enter how many elements you want:")
#print 'Enter numbers in array: '
#for i in range(int(3)):
 #   input ("input matrix 1 line: " ) a

#num_array[:, i]


   # n = input("num :")
    #num_array.append(int(n))
#print 'ARRAY: ',num_array
#print(num_array)