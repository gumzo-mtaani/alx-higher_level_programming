'''
WARNING! To run code, remember to uncomment sections that you need to run, comment out the rest!
'''



'''
Task 1: Get user name and assign to a variable then print out hello followed by the name

'''


# Ask the user to input their name and assign it to a variable name
#name = input('What is your name?')

#Print out hello followed by the name the user entered
#print('Hello ', name)


'''
Task 2: Ask user for two numbers and perform different arithmetic operations on them

'''
#Ask user to input 2 values and store them in variables num1 and num2
num1, num2 = input('Enter 2 numbers: ').split()

#Convert the strings into regular numbers (Integers)
num1 = int(num1)
num2 = int(num2)

#Add the values and store in variable addition
addition = num1 + num2

#Subtract the values and store in variable difference
difference = num1 - num2

#Multiply the values and store in variable product
product = num1 * num2

#Divide the values and store in variable quotient
quotient = num1 / num2

#Get the modulus of the two values and store in variable remainder
modulus = num1 % num2

#Print the results
print("{} + {} = {}".format(num1, num2, addition))
print("{} - {} = {}".format(num1, num2, difference))
print("{} * {} = {}".format(num1, num2, product))
print("{} / {} = {}".format(num1, num2, quotient))
print("{} % {} = {}".format(num1, num2, modulus))
