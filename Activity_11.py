
def add(a, b):
    return a+b

def display(x,y,z):
    print("{0} + {1} = {2}".format(x,y,z))
    
def main():
    a = input_number()
    b = input_number()
    summation = add(a,b)
    display(a,b,summation)
    
main()
