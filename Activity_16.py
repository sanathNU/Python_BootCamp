# function for parsing input
def parse_input(stuff):
    list1= stuff.split(';')
    list2 = [x.split('=') for x in list1]
    return list2

# function for returning input string
def take_input():
    return input()

# function for making the tuples
def make_tuples(simple_list):
    d = [(x[0],x[1]) for x in simple_list]
    return d

def main():
    a = take_input()
    b = parse_input(a)
    c = make_tuples(b)
    print(c)
    
main()
