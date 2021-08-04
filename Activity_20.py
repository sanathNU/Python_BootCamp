#Similarly as previous problem i am assuming the values to be integers. Based on that I the code will change.
# trial input:
# 45 32 789 876
# 1024 553 235 756
def take_input():
    return input().split()

#forms dictorinary of asii value and hence a different criterion for sorting
def form_dict( list1 , list2 ):
    a = {list1[i]:list2[i] for i in range(len(list1))}
    return a

def sorted_dict(a):
    c = {k:v for k,v in sorted(a.items(), key = lambda item: item[1])} #simpler and uses both dictionary comprehension and the idea of lambda as key in sorted function
    return c

def display(dictA,dictB):
    print("Original dictionary :", dictA)
    print('Sorted Dictionary :', dictB)
    
def main():
    key_list = take_input()
    value_list = take_input()
    main_dict = form_dict(key_list,value_list)
    final_dict = sorted_dict(main_dict)
    display(main_dict,final_dict)

if __name__ == '__main__':
    main()
