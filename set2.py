# # # # # # # # # # # # # # # # # # # # # # # # # print("Hello, World!")
# # # # # # # # # # # # # # # # # # # # # # # # # print('hi')
# # # # # # # # # # # # # # # # # # # # # # # # # 1. Positive or negative number: input an integer, print whether it’s positive, negative, or
# # # # # # # # # # # # # # # # # # # # # # # # # zero.
# # # # # # # # # # # # # # # # # # # # # # # # number = int(input("enter any number"))
# # # # # # # # # # # # # # # # # # # # # # # # if number>0:
# # # # # # # # # # # # # # # # # # # # # # # #     print("possitive number")
# # # # # # # # # # # # # # # # # # # # # # # # elif number<0:
# # # # # # # # # # # # # # # # # # # # # # # #     print("negetive number")
# # # # # # # # # # # # # # # # # # # # # # # # else:
# # # # # # # # # # # # # # # # # # # # # # # #      print("zero")
# # # # # # # # # # # # # # # # # # # # # # # Even or odd: check if a number is divisible by 2.
# # # # # # # # # # # # # # # # # # # # # # number = int(input("any number = "))
# # # # # # # # # # # # # # # # # # # # # # if number % 2 == 0:
# # # # # # # # # # # # # # # # # # # # # #     print("even number") 
# # # # # # # # # # # # # # # # # # # # # # else:
# # # # # # # # # # # # # # # # # # # # # #     print("odd number")

# # # # # # # # # # # # # # # # # # # # # # 3. Largest of two numbers: compare two numbers using if / else.
# # # # # # # # # # # # # # # # # # # # #  number1 = float(input("enter first number = "))
# # # # # # # # # # # # # # # # # # # # #  number2 = float(input("enter second number = "))
# # # # # # # # # # # # # # # # # # # # #  if number1> number2:
# # # # # # # # # # # # # # # # # # # # #     print("number1 is big number",number1)
# # # # # # # # # # # # # # # # # # # # #  else:
# # # # # # # # # # # # # # # # # # # # #     print("number2 is a big number",number2)
# # # # # # # # # # # # # # # # # # # # # # another
# # # # # # # # # # # # # # # # # # # # # num1 = float(input("Enter first number: "))
# # # # # # # # # # # # # # # # # # # # # num2 = float(input("Enter second number: "))

# # # # # # # # # # # # # # # # # # # # # if num1 > num2:
# # # # # # # # # # # # # # # # # # # # #     print("The largest number is:", num1)
# # # # # # # # # # # # # # # # # # # # # else:
# # # # # # # # # # # # # # # # # # # # #     print("The largest number is:", num2)

# # # # # # # # # # # # # # # # # # # # # lets begin number 4::::::::
# # # # # # # # # # # # # # # # # # # # 4. Largest of three numbers: use nested if to find the maximum of three.
# # # # # # # # # # # # # # # # # # # # num1 = float(input("enter first number"))
# # # # # # # # # # # # # # # # # # # # num2 = float(input("enter second number"))
# # # # # # # # # # # # # # # # # # # # num3 = float(input("enter third number"))
# # # # # # # # # # # # # # # # # # # # if num1 >= num2:
# # # # # # # # # # # # # # # # # # # #     if num1 >= num3:
# # # # # # # # # # # # # # # # # # # #         largest = num1
# # # # # # # # # # # # # # # # # # # #     else:
# # # # # # # # # # # # # # # # # # # #         largest = num3
# # # # # # # # # # # # # # # # # # # # else:
# # # # # # # # # # # # # # # # # # # #     if num2 >= num3:
# # # # # # # # # # # # # # # # # # # #         largest = num2
# # # # # # # # # # # # # # # # # # # #     else:
# # # # # # # # # # # # # # # # # # # #         largest = num3
# # # # # # # # # # # # # # # # # # # # print("the largest value is = ",largest)
# # # # # # # # # # # # # # # # # # #     #   5. Smallest of three numbers: similar, but find minimum.
# # # # # # # # # # # # # # # # # # # num1 = float(input("Enter first number: "))
# # # # # # # # # # # # # # # # # # # num2 = float(input("Enter second number: "))
# # # # # # # # # # # # # # # # # # # num3 = float(input("Enter third number: "))

# # # # # # # # # # # # # # # # # # # if num1 <= num2:
# # # # # # # # # # # # # # # # # # #     if num1 <= num3:
# # # # # # # # # # # # # # # # # # #         smallest = num1
# # # # # # # # # # # # # # # # # # #     else:
# # # # # # # # # # # # # # # # # # #         smallest = num3
# # # # # # # # # # # # # # # # # # # else:
# # # # # # # # # # # # # # # # # # #     if num2 <= num3:
# # # # # # # # # # # # # # # # # # #         smallest = num2
# # # # # # # # # # # # # # # # # # #     else:
# # # # # # # # # # # # # # # # # # #         smallest = num3

# # # # # # # # # # # # # # # # # # # print("The smallest number is:", smallest)

# # # # # # # # # # # # # # # # # #         6. Character is vowel or consonant: check using if or switch.
# # # # # # # # # # # # # # # # # character = input("Enter a character: ").lower()
# # # # # # # # # # # # # # # # # if character in ['a', 'e', 'i', 'o', 'u']:
# # # # # # # # # # # # # # # # #     print("The character is a vowel.")
# # # # # # # # # # # # # # # # # else:    print("The character is a consonant.")


# # # # # # # # # # # # # # # # char = input("Enter a character: ")

# # # # # # # # # # # # # # # # if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u' or \
# # # # # # # # # # # # # # # #    char == 'A' or char == 'E' or char == 'I' or char == 'O' or char == 'U':
# # # # # # # # # # # # # # # #     print("It is a vowel")
# # # # # # # # # # # # # # # # else:
# # # # # # # # # # # # # # # #     print("It is a consonant")
# # # # # # # # # # # # # # # #        7. Character is uppercase, lowercase, digit, or special symbol: check ASCII ranges.

# # # # # # # # # # # # # # # char = input("Enter a character: ")

# # # # # # # # # # # # # # # ascii_value = ord(char)

# # # # # # # # # # # # # # # if ascii_value >= 65 and ascii_value <= 90:
# # # # # # # # # # # # # # #     print("Uppercase letter")
# # # # # # # # # # # # # # # elif ascii_value >= 97 and ascii_value <= 122:
# # # # # # # # # # # # # # #     print("Lowercase letter")
# # # # # # # # # # # # # # # elif ascii_value >= 48 and ascii_value <= 57:
# # # # # # # # # # # # # # #     print("Digit")
# # # # # # # # # # # # # # # else:
# # # # # # # # # # # # # # #     print("Special symbol")
# # # # # # # # # # # # # # #    8. Check divisibility by 5 and 11: print “Divisible by both” / “Not divisible”.

# # # # # # # # # # # # # # num = int(input("Enter a number: "))
# # # # # # # # # # # # # # if num % 5 == 0 and num % 11 == 0:
# # # # # # # # # # # # # #     print("Divisible by both")
# # # # # # # # # # # # # # else:
# # # # # # # # # # # # # #     print("Not divisible")

# # # # # # # # # # # # # #     year = int(input("Enter a year: "))
# # # # # # # # # # # # # # if year % 4 == 0:
# # # # # # # # # # # # # #     if year % 100 == 0:
# # # # # # # # # # # # # #         if year % 400 == 0:
# # # # # # # # # # # # # #             print("Leap year")
# # # # # # # # # # # # # #         else:
# # # # # # # # # # # # # #             print("Not a leap year")
# # # # # # # # # # # # # #     else:
# # # # # # # # # # # # # #         print("Leap year")
# # # # # # # # # # # # # # else:
# # # # # # # # # # # # # #     print("Not a leap year")

# # # # # # # # # # # # #        9. Check leap year: apply leap-year rule using nested if.

# # # # # # # # # # # # year = int(input("Enter a year: "))
# # # # # # # # # # # # if year % 4 == 0:
# # # # # # # # # # # #     print("Leap year")
# # # # # # # # # # # #     if year % 100 == 0:
# # # # # # # # # # # #         print("Century year")
# # # # # # # # # # # #         if year % 400 == 0:
# # # # # # # # # # # #             print("Also a leap year")
# # # # # # # # # # # #         else:
# # # # # # # # # # # #             print("Not a leap year")

# # # # # # # # # # # year = int(input("Enter a year: "))
# # # # # # # # # # # if year % 4 == 0:
# # # # # # # # # # #     if year % 100 == 0:
# # # # # # # # # # #         if year % 400 == 0:
# # # # # # # # # # #             print("Leap year")
# # # # # # # # # # #         else:
# # # # # # # # # # #             print("Not a leap year")
# # # # # # # # # # #     else:
# # # # # # # # # # #         print("Leap year")
# # # # # # # # # # # else:
# # # # # # # # # # #     print("Not a leap year")

# # # # # # # # # # #      Check whether a person is eligible to vote: age ≥ 18 then eligible.

# # # # # # # # # # age = int(input("Enter your age: "))

# # # # # # # # # # if age >= 18:
# # # # # # # # # #     print("Eligible to vote")
# # # # # # # # # # else:
# # # # # # # # # #     print("Not eligible to vote")

# # # # # # # # # #     11. Check whether a student passed or failed: marks ≥ 40 then pass.
# # # # # # # # # marks = int(input("Enter marks: "))

# # # # # # # # # if marks >= 40:
# # # # # # # # #     print("Pass")
# # # # # # # # # else:
# # # # # # # # #     print("Fail")
# # # # # # # # #      12. Find grade based on marks: use multiple else if conditions for A, B, C, etc.

# # # # # # # # marks = float(input("Enter the marks: "))

# # # # # # # # if marks > 100 or marks < 0:
# # # # # # # #     print("Invalid input.")
# # # # # # # # elif marks >= 90:
# # # # # # # #     print("Grade: A")
# # # # # # # # elif marks >= 80:
# # # # # # # #     print("Grade: B")
# # # # # # # # elif marks >= 70:
# # # # # # # #     print("Grade: C")
# # # # # # # # elif marks >= 60:
# # # # # # # #     print("Grade: D")
# # # # # # # # else:
# # # # # # # #     print("Grade: F")

# # # # # # #      #13. Find absolute value of a number: if negative, multiply by -1.
# # # # # # # num = float(input("Enter a number: "))
# # # # # # # if num < 0:
# # # # # # #     num = num * -1
# # # # # # # print("Absolute value:", num)
# # # # # # # 14. Check if a number is a multiple of another: use modulus operator.
# # # # # # a = int(input("First number: "))
# # # # # # b = int(input("Second number: "))

# # # # # # if a % b == 0:
# # # # # #     print("Multiple")
# # # # # # else:
# # # # # #     print("Not Multiple")


# # # # # first_number = int(input("Enter the first number: "))
# # # # # second_number = int(input("Enter the second number: "))


# # # # # if first_number % second_number == 0:
# # # # #     print(first_number, "is a multiple of", second_number)
# # # # # else:
# # # # #     print(first_number, "is not a multiple of", second_number)

# # # # #         15. Check if three sides can form a triangle: use triangle inequality rule.

# # # # a = int(input("First side: "))
# # # # b = int(input("Second side: "))
# # # # c = int(input("Third side: "))

# # # # if a + b > c and a + c > b and b + c > a:
# # # #     print("Triangle can be formed")
# # # # else:
# # # #     print("Triangle cannot be formed")
# # # #         16. Check if triangle is equilateral, isosceles, or scalene: compare sides.

# # # a = float(input("Enter first side: "))
# # # b = float(input("Enter second side: "))
# # # c = float(input("Enter third side: "))


# # # if a == b and b == c:
# # #     print("The triangle is Equilateral")
# # # elif a == b or b == c or a == c:
# # #     print("The triangle is Isosceles")
# # # else:
# # #     print("The triangle is Scalene")
# # #        17. Check whether a character is an alphabet or not: ASCII check


# # char = input("Enter a character: ")
# # ascii_value = ord(char)
# # if (ascii_value >= 65 and ascii_value <= 90) or (ascii_value >= 97 and ascii_value <= 122):
# #     print("The character is an alphabet.")
# # else:
# #     print("The character is not an alphabet.")
# #        18. Check whether a year is a century year: year % 100 == 0.

# year = int(input("Enter a year: "))
# if year % 100 == 0:
#     print("It is a century year.")
# else:
#     print("It is not a century year.")

#     19. Check if person is eligible for discount: based on age or purchase amount.
age = int(input("Enter your age: "))
purchase_amount = float(input("Enter purchase amount: "))
if age >= 60 or purchase_amount > 1000:
    print("Eligible for discount")
else:
    print("Not eligible for discount")

