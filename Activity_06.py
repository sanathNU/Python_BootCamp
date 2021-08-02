a = input().split()
b = a[:3]
c = a[:]
print("sliced list =",b)

a[0]=a[-1]=b[0]=b[-1]=0
print("replaced list-1 =",a)
print("replaced list-2 =",b)

#challenge
print("reversed list",c[::-1])
