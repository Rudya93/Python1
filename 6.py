#def caesarCipher():
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




print('Hello'.replace('l', 'L'))
# вернёт 'HeLLo'


print('Abrakadabra'.replace('a', 'A', 2))
# вернёт 'AbrAkAdabra'



    #key(number)