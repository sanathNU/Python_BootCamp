# This function takes input of an angle and outputs the sin of that angle using McLauren Series
# Eg Input 56 degrees


# This function takes input of an angle and outputs the sin of that angle using McLauren Series
# Formula sin(x) = x - x^3/3! +x^5/5! -x^7/7!.....
# I have taken only upto 5 terms..to get more accuracy, increase numbers on terms n
# Eg Input 56 degrees

import math
#Let 10 be the default number of terms

def sinX(theta,n=10):
    sin,flag = 0,1
    #this functions contains lot of redundant variables and printf functions, will show the actual working of the code, could be imporved in the future
    for i in range(1,n,2):
        ten = pow(theta,i)*flag/math.factorial(i)
        print("%f + %f = %f"%(sin,ten,sin+ten))
        sin +=ten
        flag = -flag
    return sin

def DegToTheta(a):
    return (a*math.pi)/180

def main():
    print("Enter the input angle in degrees:")
    a = int(input())
    b = DegToTheta(a); print(b)
    c = sinX(b,12)
    print("The value of of sin of %d is %.9f" %(a,c)) #Only outputting till 9 decimal digits
    
main()
