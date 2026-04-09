# # # # # # # # # # # print("Hello, World!")
# # # # # # # # # # # print('hi')
# # # # # # # # # # # 1. Positive or negative number: input an integer, print whether it’s positive, negative, or
# # # # # # # # # # # zero.
# # # # # # # # # # number = int(input("enter any number"))
# # # # # # # # # # if number>0:
# # # # # # # # # #     print("possitive number")
# # # # # # # # # # elif number<0:
# # # # # # # # # #     print("negetive number")
# # # # # # # # # # else:
# # # # # # # # # #      print("zero")
# # # # # # # # # Even or odd: check if a number is divisible by 2.
# # # # # # # # number = int(input("any number = "))
# # # # # # # # if number % 2 == 0:
# # # # # # # #     print("even number") 
# # # # # # # # else:
# # # # # # # #     print("odd number")

# # # # # # # # 3. Largest of two numbers: compare two numbers using if / else.
# # # # # # #  number1 = float(input("enter first number = "))
# # # # # # #  number2 = float(input("enter second number = "))
# # # # # # #  if number1> number2:
# # # # # # #     print("number1 is big number",number1)
# # # # # # #  else:
# # # # # # #     print("number2 is a big number",number2)
# # # # # # # # another
# # # # # # # num1 = float(input("Enter first number: "))
# # # # # # # num2 = float(input("Enter second number: "))

# # # # # # # if num1 > num2:
# # # # # # #     print("The largest number is:", num1)
# # # # # # # else:
# # # # # # #     print("The largest number is:", num2)

# # # # # # # lets begin number 4::::::::
# # # # # # 4. Largest of three numbers: use nested if to find the maximum of three.
# # # # # # num1 = float(input("enter first number"))
# # # # # # num2 = float(input("enter second number"))
# # # # # # num3 = float(input("enter third number"))
# # # # # # if num1 >= num2:
# # # # # #     if num1 >= num3:
# # # # # #         largest = num1
# # # # # #     else:
# # # # # #         largest = num3
# # # # # # else:
# # # # # #     if num2 >= num3:
# # # # # #         largest = num2
# # # # # #     else:
# # # # # #         largest = num3
# # # # # # print("the largest value is = ",largest)
# # # # #     #   5. Smallest of three numbers: similar, but find minimum.
# # # # # num1 = float(input("Enter first number: "))
# # # # # num2 = float(input("Enter second number: "))
# # # # # num3 = float(input("Enter third number: "))

# # # # # if num1 <= num2:
# # # # #     if num1 <= num3:
# # # # #         smallest = num1
# # # # #     else:
# # # # #         smallest = num3
# # # # # else:
# # # # #     if num2 <= num3:
# # # # #         smallest = num2
# # # # #     else:
# # # # #         smallest = num3

# # # # # print("The smallest number is:", smallest)

# # # #         6. Character is vowel or consonant: check using if or switch.
# # # character = input("Enter a character: ").lower()
# # # if character in ['a', 'e', 'i', 'o', 'u']:
# # #     print("The character is a vowel.")
# # # else:    print("The character is a consonant.")


# # char = input("Enter a character: ")

# # if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u' or \
# #    char == 'A' or char == 'E' or char == 'I' or char == 'O' or char == 'U':
# #     print("It is a vowel")
# # else:
# #     print("It is a consonant")
# #        7. Character is uppercase, lowercase, digit, or special symbol: check ASCII ranges.

# char = input("Enter a character: ")

# ascii_value = ord(char)

# if ascii_value >= 65 and ascii_value <= 90:
#     print("Uppercase letter")
# elif ascii_value >= 97 and ascii_value <= 122:
#     print("Lowercase letter")
# elif ascii_value >= 48 and ascii_value <= 57:
#     print("Digit")
# else:
#     print("Special symbol")
#    8. Check divisibility by 5 and 11: print “Divisible by both” / “Not divisible”.

num = int(input("Enter a number: "))
if num % 5 == 0 and num % 11 == 0:
    print("Divisible by both")
else:
    print("Not divisible")

    year = int(input("Enter a year: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not a leap year")
    else:
        print("Leap year")
else:
    print("Not a leap year")




