#The main difference between sort and sorted is that
# sort() is a method and sorted is a function
# sort modifies the original list itself whereas sorted returns a new list of sorted values

def input_string():
    lis = [char for char in input().split()]
    return lis

def sort_using_meth(word):
    word.sort()  # the original list is modified
    return word

def sort_using_func(word):
    return sorted(word)

def main():
    string1 = input_string()
    print(sort_using_func(string1), string1) # printing sorted and original function....each list should be different
    print(sort_using_meth(string1), string1) # since the original function is changed, both output should be the same

main()
