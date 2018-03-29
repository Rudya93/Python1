a = [1, 2, 3, 4, 5, 6]
a = a[1:] + [0]
print (a)


a = [1, 2, 3, 4, 5, 6]
i = 0
while i < len(a) - 1:
    a[i] = a[i + 1]
    i += 1
a[i] = 0