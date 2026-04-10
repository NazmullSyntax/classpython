# # # # # # # # # # # # print("welcome to set3.py")
# # # # # # # # # # # #     1. Print numbers from 1 to N: simple counting loop

# # # # # # # # # # # n = int(input("Enter a number: "))

# # # # # # # # # # # for i in range(1, n + 1):
# # # # # # # # # # #     print(i)

# # # # # # # # # # #     2. Print numbers from N down to 1: reverse counting.

# # # # # # # # # # n = int(input("Enter a number: "))

# # # # # # # # # # for i in range(n, 0, -1):
# # # # # # # # # #     print(i)

# # # # # # # # # # 3. Print even numbers from 1 to N.

# # # # # # # # # n = int(input("Enter a number: "))

# # # # # # # # # for i in range(2, n + 1, 2):
# # # # # # # # #     print(i)

# # # # # # # # #     # 4. Print odd numbers from 1 to N.
# # # # # # # # # n = int(input("Enter a number: "))

# # # # # # # # # for i in range(1, n + 1, 2):
# # # # # # # # #     print(i)

# # # # # # # # #     5. Print sum of first N natural numbers.
# # # # # # # # n = int(input("Enter a number: "))

# # # # # # # # total = 0

# # # # # # # # for i in range(1, n + 1):
# # # # # # # #     total += i

# # # # # # # # print("Sum =", total)

# # # # # # # # 6. Print sum of even numbers from 1 to N.
# # # # # # # n = int(input("Enter a number: "))

# # # # # # # total = 0

# # # # # # # for i in range(2, n + 1, 2):
# # # # # # #     total += i

# # # # # # # print("Sum of even numbers =", total)

# # # # # # # # 7. Print sum of odd numbers from 1 to N.
# # # # # # # n = int(input("Enter a number: "))
# # # # # # # total = 0
# # # # # # # for i in range(1, n + 1, 2):
# # # # # # #     total += i

# # # # # # # print("Sum of odd numbers =", total)

# # # # # # 8. Print multiplication table for any number.
# # # # # n = int(input("enter value"))

# # # # # for i in range(1, 11):
# # # # #     print(n * i)
# # # # #       9. Count digits in a number.
# # # # n = int(input("enter value"))
# # # # count = 0

# # # # while n > 0:
# # # #     n = n // 10
# # # #     count += 1
# # # # print("Number of digits =", count)
# # # n = len(input("enter value = "))
# # # print("Number of digits =", n)
# # # 10. Find sum of digits in a number
# # n = int(input("enter value"))
# # total = 0
# # while n > 0:
# #     digit = n % 10
# #     total += digit
# #     n = n // 10
# # print("Sum of digits =", total)

# see another solution for 10. Find sum of digits in a number
n = (input("enter digits: "))
total = 0
for digit in n:
    total += int(digit)
print("Sum of digits =", total)










