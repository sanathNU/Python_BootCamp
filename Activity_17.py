# I'm assuming the intput will be given as in triple quotes ''' [('system', 's'), ('database', 'd'), ('username', 'u'), ('password', 'p')] '''
# kinda interesting...i'm going to use regex to remove unwanted alphanumberic characters
import re

# This function cleans the input and returns a list of strings
# for my reference [^\w] means remove stuff that are not alphanumeric characters
def clean_input(stuff):
    string1 = re.sub(r'[^\w]',' ',stuff)
    list1 = string1.split()
    return list1

#This function takes the cleaned list and makes the final required word
def make_string(more_stuff):
    i=0 
    list2=[]    # making another list of the required tuples for more easy working
    while( i<len(more_stuff)-1):
        word = more_stuff[i]+'=' + more_stuff[i+1]
        list2.append(word)
        i=i+2
    final_word = ';'.join(list2)
    return final_word

def main():
    a = input()
    b = clean_input(a)
    c = make_string(b)
    print(c)

main()
