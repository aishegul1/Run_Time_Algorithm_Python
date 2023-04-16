#solution by Riya

import time #import time

start = time.time()
#creates list, map executes in an iterable
#float represents the real numbers, and input allows te user to insert value
#split seperates a string and arranges them in list
list1 = list(map(float, input('Please enter your float numbers with space: ').split()))

def max_three(list1): #defining the function
  list1.sort(reverse=True) #sorts the elements in the list in descending order
  return list1[:3]

print(max_three(list1))
end = time.time() #returns the time as expressed in seconds passed
print(f"Runtime: {end - start}") #prints runtime