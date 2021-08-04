#I am assuming that keys are integers and sorted them according to that. There is another function which sorts according to ASCII
# trial input:
# 45 32 789 876
# a b c d
#dictionary should be stored in format {1:a, 2:b, 3: c, 4:d}
#Edit: Used dictionary comprehension instead of using for loops and all...it was a clear learning experience
def take_input():
    return input().split()

#forms dictorinary of asii value and hence a different criterion for sorting
def form_ascii_dict( list1 , list2 ):
    a = {list1[i]:list2[i] for i in range(len(list1))}
    return a

#forms dictionary using int. This is the default function used in this program
def form_int_dict( list1, list2 ):
    b = {int(list1[i]):list2[i] for i in range(len(list1))}
    return b

def sorted_dict(a):
    b = { items:a[items] for items in sorted(a)}
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
