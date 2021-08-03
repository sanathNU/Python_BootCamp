#program to add
a = int(input())
b = int(input())

# 3 methods of displaying the string
print(a,"+",b,"=",a+b)
print("{0} + {1} = {2}".format(a,b,a+b))   #format function using number lettering
print("{x} + {y} = {z}".format(z = a+b, x =a, y = b)) #format function using string handlers
print(a , "+",b,"= %d" %(a+b))            # using the old C format
