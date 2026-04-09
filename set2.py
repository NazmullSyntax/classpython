# # # # # # print("Hello, World!")
# # # # # # print('hi')
# # # # # # 1. Positive or negative number: input an integer, print whether it’s positive, negative, or
# # # # # # zero.
# # # # # number = int(input("enter any number"))
# # # # # if number>0:
# # # # #     print("possitive number")
# # # # # elif number<0:
# # # # #     print("negetive number")
# # # # # else:
# # # # #      print("zero")
# # # # Even or odd: check if a number is divisible by 2.
# # # number = int(input("any number = "))
# # # if number % 2 == 0:
# # #     print("even number") 
# # # else:
# # #     print("odd number")

# # # 3. Largest of two numbers: compare two numbers using if / else.
# #  number1 = float(input("enter first number = "))
# #  number2 = float(input("enter second number = "))
# #  if number1> number2:
# #     print("number1 is big number",number1)
# #  else:
# #     print("number2 is a big number",number2)
# # # another
# # num1 = float(input("Enter first number: "))
# # num2 = float(input("Enter second number: "))

# # if num1 > num2:
# #     print("The largest number is:", num1)
# # else:
# #     print("The largest number is:", num2)

# # lets begin number 4::::::::
# 4. Largest of three numbers: use nested if to find the maximum of three.
num1 = float(input("enter first number"))
num2 = float(input("enter second number"))
num3 = float(input("enter third number"))
if num1 >= num2:
    if num1 >= num3:
        largest = num1
    else:
        largest = num3
else:
    if num2 >= num3:
        largest = num2
    else:
        largest = num3
print("the largest value is = ",largest)





