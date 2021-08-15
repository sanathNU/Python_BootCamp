mport copy
table = {0:'',1:'',2:'abc',3:'def',4:'ghi',5:'jkl',6:'mno',7:'pqrs',8:'tuv',9:'wxyz'}

def input_stuff():
    return list(map(int,list(input())))

#for 1st type of operation
#   A(a)
#   |
#   B(ad)
def func0(i,output,count):
    if i==0 or i==1:
        return ''
    ten = table[i][count]
    output = [out+ten for out in output ]
    return output

#done for 2nd type of operations
#   A(adgg)
#  /        \
# B(adggg)  C(adgh)
def func1(i,x,count):
    a= copy.deepcopy(x)
    b = copy.deepcopy(x)
    b = [x[:-1] for x in b]
    a=func0(i,a,count)
    b=func0(i,b,count+1)
    return a,b

#done for 3rd type of operation
#   A(ad)
#   /    \
# B(adgg) C(adh)
def func2(i,x,count):
    a = copy.deepcopy(x)
    b = copy.deepcopy(x)
    a=func0(i,a,count)
    a=func0(i,a,count)
    b=func0(i,b,count+1)
    return a,b

#done for 4th type of operation
#   A(adh)
#  /      \
# B(adhg)  C(adk)
def func3(i,x,count):
    a = copy.deepcopy(x)
    b = copy.deepcopy(x)
    b = [x[:-1] for x in b]
    a =func0(i,a,count)
    b =func0(i,b,count+2)
    return a,b

def state1(i,a):
    # print(a)
    b = func0(i,a,0)
    return b

def state2(i,a):
    x,y = func2(i,a,0)
    return x+y

def state3(i,a):
    print(a[-2],a[-1])
    x = [a[-2]]
    y = [a[-1]]
    list1=func1(i,x,0)
    list2=func3(i,y,0)
    list1 = [x[0] for x in list1]
    list2 = [x[0] for x in list2]

    return list1+list2

def find_out(num,n):
    output=['']
    state,dl=1,0
    for i in range(n):
        
        if i<n-1:
            test = num[i]==num[i+1]  # Our testing loop
        else:
            test = False
        print(state,dl)
        if dl==1 and not test:
            print('loop skipped!')
            dl=0
            continue
        if state==1:
            if test:
                state=2
                output=state2(num[i],output)
                dl=1
                continue
            else:
                state=1
                output=state1(num[i],output)
        
        if state==2:
            if test:
                state=3
                print('in state2',state)
                output=state3(num[i],output)
                continue
            else:
                state=1
                output =state1(num[i],output)
                continue
                
        if state==3:
            if test and num[i]==9:
                print("You can't enter here!")
                output=['']
                #It is the case of w so..let is be for now
                pass
            else:
                state=1
                output =state1(num[i],output)

        print('Output of every loop',output,state)
    return output
            
        
def main():
    num = input_stuff()
    output = find_out(num,len(num))
    print('The Final Output is',output)

main()
