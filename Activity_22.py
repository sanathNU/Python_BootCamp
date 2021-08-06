# This function takes input of an angle and outputs the sin of that angle using McLauren Series
# Eg Input 56 degrees

import math
#Let 10 be the default number of terms

def sinX(theta,n=10):
    sin = 0
    for i in range(n,2):
        sin += pow(theta,i)/math.factorial(i)
        print("value of sin is",sin)
    return sin

def DegToTheta(a):
    return (a*math.pi)/180

def main():
    print("Enter the input angle in degrees:")
    a = int(input())
    b = DegToTheta(a); print(b)
    c = sinX(b)
    print("The value of of sin of %d is %d" %(a,c))
    
main()
