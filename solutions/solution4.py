import time

start = time.time()

#input takes the number from user, split is used to separates these numbers
#separated numbers are string so convert them to float and make a list
numbers = [float(number) for number in input('Enter numbers separated by spaces: ').split(' ')]
max_num = max(numbers)

print("DISPLAY........") #displaying all numbers which a users has inserted
for i in range(len(numbers)):
	print(f'Number {i+1}: {numbers[i]}')
print("Largest number is : ", max_num) #displaying the largest number

end = time.time() #stops the runtime
print(f"Runtime: {end - start}") #prints runtime