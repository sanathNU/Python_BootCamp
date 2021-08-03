#I am assuming that keys are integers and sorted them according to that. There is another function which sorts according to ASCII
# trial input:
# 45 32 789 876
# a b c d
#dictionary should be stored in format {1:a, 2:b, 3: c, 4:d}
def take_input():
    return input().split()

#forms dictorinary of asii value and hence a different criterion for sorting
def form_ascii_dict( list1 , list2 ):
    a ={}
    for i in range(len(list1)):
        a[list1[i]] = list2[i]
    return a

#forms dictionary using int. This is the default function used in this program
def form_int_dict( list1, list2 ):
    b={}
    list1 = [ int(x) for x in list1]
    for i in range(len(list1)):
        b[list1[i]] = list2[i]
    return b


def sorted_dict(a):
    b = {}
    for items in sorted(a.keys()):
        b[items] =a[items]
    return b

def display(dictA,dictB):
    print("Original dictionary :", dictA)
    print('Sorted Dictionary :', dictB)
    
def main():
    key_list = take_input()
    value_list = take_input()
    main_dict = form_int_dict(key_list,value_list)
    final_dict = sorted_dict(main_dict)
    display(main_dict,final_dict)

if __name__ == '__main__':
    main()
