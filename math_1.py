'''GETTING INPUT FROM USER FOR COMPUTE SOME MATH OPRATIONS'''
import math
#collecting information
num = input("Enter a number:")
num = float(num)
#calculating log2(n)
print("\nyour log2(n) value is:")
print(math.log2(num))
print("\nyour cos(n) value is:")
print(math.cos(num))
#calculating e^n value
print("\nthe exponential of your number is:")
print(math.exp(num))