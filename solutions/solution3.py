# 3rd soluation from by Aysegul Kayikci
import time
#import time module
start = time.time()

#import from random numbers for numbers list
import random
def get_max(lst, exlcuded= []): #empty list
    max = lst[0] #list starts from zero and gives 1st value.
    for i in lst:
        if i > max and not i in exlcuded:
            max = i
    return max

def sol_max_three(lst):
    lst.sort(reverse=1)
    return lst[:3]
#return list, and gives just 3 numbers in the list.

#this function gives/print the maximum 3 numbers in the number list.
def get_max_three(lst):
    max = get_max(lst) #gets 1st highest number in the list.
    mid = get_max(lst, [max]) #gets 2nd highest number in the list.
    min = get_max(lst, [max, mid]) #gets 3rd highest number in the list.
    return [max, mid, min]

test1 =  [int(random.random())] #here is our integer, user can change numbers from here.
tests = [test1]
print(sol_max_three([1124.71, 5459.43, 7324.98, 2963]))
# Code be able to accept any float number.
end = time.time() #stops the runtime.
print(f"Runtime: {end - start}") #prints the runtime.