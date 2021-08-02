def inputa(): 
    print("Enter only numbers:\n")
    a = list(map(int,input().split()))
    return a                          

def easy_met(a):
    return max(a)

def if_else(a):
    if a[0] >= a[1] and a[0] >= a[2]:
        return a[0]
    elif a[1]>=a[0] and a[1]>=a[2]:
        return a[1]
    else: 
        return a[2]
        
def bubble_sort_mode(a):
    for first in range(len(a)):
        for second in range(first+1,len(a)):
            if(a[first]<a[second]):
                a[first],a[second] = a[second],a[first] #Using Bubble sort        
    print("The Greatest Number is",a[0])      #Using Bubble sort
    
def main():
    a = inputa()
    print(easy_met(a),if_else(a),bubble_sort_mode(a))
    

main()
