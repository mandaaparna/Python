import random
str1 = input("Please enter the input string")
del_char1_ind = random.randint(0, len(str1)-1)
str1 = str1.replace(str1[del_char1_ind], '')
del_char2_ind = random.randint(0, len(str1)-1)
str1 = str1.replace(str1[del_char2_ind], '')
str1 = str1[::-1]
print(str1)

x = int(input("Enter first number:"))
y = int(input("Enter second number:"))
print("Adiition is:" , x+y)
print("Subtraction is:", x-y)
print("multiplication is:", x*y)
print("Division is:", x/y)
print("Modulus is:", x%y)

str2 = input("Please enter the input string")
str2 = str2.replace('python', 'pythons')
print(str2)