#The forumula is Vol = (b^2 * h^2)/(sqrt(l^2+b^2+h^2))

print("Enter the values of length,breadth and height in same order respectively: \n")
a = list(map(int,input().split()))
l,b,h = a
volTromb =( pow(b,2) * pow(h,2) )/ pow( pow(l,2)+pow(b,2)+pow(h,2),0.5)
radCirc = pow((volTromb *3)/(4*3.1415),1/3)
#Volume of Troboloid
print("{:0.3f}".format(volTromb))
#radius of the sphere
print("{:0.3f}".format(radCirc))
