# Given Input s=system;d=database;u=username;p=password

#takes input
def take_input():
    return input()
#cleans input and gives out a string
def parse_input(a):
    list1 = list(a.split(';'))
    list2 = [x.split('=') for x in list1]
    return list2
#the input can be used to convert to dictionary
def convert_dict(stuff):
    final_dict = {}
    for lists in stuff:
        final_dict[lists[0]] =lists[1]
    return final_dict
#converting back from dictionary to string
def challenge_part(dictionary):
    list1 =[]
    for key,value in dictionary.items():
        word = key +'='+value
        list1.append(word)
    final_part = ';'.join(list1)
    return final_part

def main():
    a = take_input()
    b = parse_input(a)          
    c = convert_dict(b)       #The final answer lies here
    d = challenge_part(c)     #returns the origianal dictionary normally
    print(c)

main()
