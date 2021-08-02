print("Enter only numbers:\n")
a = list(map(int,input().split()))
# print(max(a))                           //easy method

#or
for first in range(len(a)):
    for second in range(first+1,len(a)):
        if(a[first]<a[second]):
            a[first],a[second] = a[second],a[first]
        
print("The Greatest Number is",a[0])      #Using Bubble sort
