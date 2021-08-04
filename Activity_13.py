import math
def inp():    
    print("Enter only number:\n")
    a = int(input())
    return a

def prime(a):
    if a == 0 or a == 1:
        print("1 or 0 are not prime or composite numbers")
    else:
        count = 0
        numbers = []
        for i in range(2,math.floor(math.sqrt(a))):                  #Reduced the size of the bruteforce attack
            if( a%i == 0):
                count+=1
                numbers.append(str(i))
        if(count>0):
            print("Not a prime!",a,"It's factors are ",','.join(numbers))
        else:
            print("It's a prime!",a)

def main():
    a = inp()
    prime(a)
    
main()
