#1. Find the data type of every value in a mixed list

data = [10, 20.5, "Hello", True, 5+2j]

for i in data:
    print(i, ":", type(i))


#2. Convert a nested list into a tuple of tuples

lst = [[1, 2], [3, 4], [5, 6]]

result = tuple(tuple(i) for i in lst)

print(result)


#3. Remove duplicate values while preserving original order

lst = [10, 20, "Hello", 10, "Python", 20, "Hello"]

new_list = []

for i in lst:
    if i not in new_list:
        new_list.append(i)

print("List after removing duplicates:", new_list)


#4. Check whether a number is a power of 2

def power_of_two(n):
    if n > 0 and (n & (n - 1)) == 0:
        return "Power of 2"
    else:
        return "Not a power of 2"

n = int(input("Enter a number: "))
print(power_of_two(n))


#5. Swap two numbers using bitwise XOR

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

a = a ^ b
b = a ^ b
a = a ^ b

print("After swapping:")
print("a =", a)
print("b =", b)


#6. Check whether a number is divisible by both 4 and 6

def check(n):
    if n % 4 == 0 and n % 6 == 0:
        return "Divisible by both 4 and 6"
    else:
        return "Not divisible by both"

n = int(input("Enter a number: "))
print(check(n))


#7. Calculate electricity bill using different unit rates

def electricity_bill(units):
    if units < 0:
        return "Invalid units"

    elif units <= 100:
        bill = units * 2

    elif units <= 200:
        bill = 100 * 2 + (units - 100) * 3

    else:
        bill = 100 * 2 + 100 * 3 + (units - 200) * 5

    return bill

units = int(input("Enter electricity units: "))
print("Electricity Bill:", electricity_bill(units))


#8. Check whether three sides can form a triangle

def triangle(a, b, c):
    if a > 0 and b > 0 and c > 0 and a+b > c and a+c > b and b+c > a:
        return "Valid Triangle"
    else:
        return "Invalid Triangle"

a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))

print(triangle(a, b, c))


#9. Determine the type of triangle

def triangle_type(a, b, c):
    if a <= 0 or b <= 0 or c <= 0 or a+b <= c or a+c <= b or b+c <= a:
        return "Invalid Triangle"

    elif a == b and b == c:
        return "Equilateral Triangle"

    elif a == b or b == c or a == c:
        return "Isosceles Triangle"

    else:
        return "Scalene Triangle"

a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))

print(triangle_type(a, b, c))


#10. Create a simple ATM menu

balance = 5000

while True:
    print("\n1. Withdraw")
    print("2. Deposit")
    print("3. Balance")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        amount = int(input("Enter withdrawal amount: "))

        if amount > 0 and amount <= balance:
            balance = balance - amount
            print("Withdrawal successful")
        else:
            print("Invalid amount or insufficient balance")

    elif choice == 2:
        amount = int(input("Enter deposit amount: "))

        if amount > 0:
            balance = balance + amount
            print("Deposit successful")
        else:
            print("Invalid amount")

    elif choice == 3:
        print("Available Balance:", balance)

    elif choice == 4:
        print("Thank you!")
        break

    else:
        print("Invalid choice")


#11. Calculate income tax based on different tax slabs

def income_tax(income):
    if income < 0:
        return "Invalid income"

    elif income <= 250000:
        tax = 0

    elif income <= 500000:
        tax = (income - 250000) * 0.05

    elif income <= 1000000:
        tax = 250000 * 0.05 + (income - 500000) * 0.20

    else:
        tax = 250000 * 0.05 + 500000 * 0.20 + (income - 1000000) * 0.30

    return tax

income = float(input("Enter annual income: "))
print("Income Tax:", income_tax(income))


#12. Menu-driven calculator using if-elif

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter your choice: "))

if choice == 1:
    print("Result:", a + b)

elif choice == 2:
    print("Result:", a - b)

elif choice == 3:
    print("Result:", a * b)

elif choice == 4:
    if b != 0:
        print("Result:", a / b)
    else:
        print("Cannot divide by zero")

else:
    print("Invalid choice")


#13. Print all prime numbers between 1 and n

n = int(input("Enter a number: "))

for num in range(2, n + 1):
    count = 0

    for i in range(2, num):
        if num % i == 0:
            count = count + 1
            break

    if count == 0:
        print(num)


#14. Find factorial of a number using a loop

def factorial(n):
    fact = 1

    for i in range(1, n + 1):
        fact = fact * i

    return fact

n = int(input("Enter a number: "))

if n < 0:
    print("Factorial is not defined")
else:
    print("Factorial:", factorial(n))


#15. Print Fibonacci series up to n terms

n = int(input("Enter number of terms: "))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b


#16. Check whether a number is an Armstrong number

n = int(input("Enter a number: "))

temp = n
power = len(str(n))
total = 0

if n < 0:
    print("Not an Armstrong number")

else:
    while temp > 0:
        digit = temp % 10
        total = total + digit ** power
        temp = temp // 10

    if total == n:
        print("Armstrong Number")
    else:
        print("Not an Armstrong Number")


#17. Reverse a number and check whether it is a palindrome

n = int(input("Enter a number: "))

temp = n
reverse = 0

while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp = temp // 10

print("Reverse:", reverse)

if n >= 0 and n == reverse:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")


#18. Find GCD of two numbers

def gcd(a, b):
    a = abs(a)
    b = abs(b)

    while b != 0:
        a, b = b, a % b

    return a

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("GCD:", gcd(a, b))


#19. Function to check whether a string is a palindrome

def palindrome(s):
    if s == s[::-1]:
        return "Palindrome"
    else:
        return "Not Palindrome"

word = input("Enter a string: ")
print(palindrome(word))


#20. Function to count vowels and consonants

def count_letters(s):
    vowels = 0
    consonants = 0

    for i in s:
        if i.isalpha():
            if i.lower() in "aeiou":
                vowels = vowels + 1
            else:
                consonants = consonants + 1

    return vowels, consonants

word = input("Enter a string: ")

v, c = count_letters(word)

print("Vowels:", v)
print("Consonants:", c)


#21. Function to calculate Simple and Compound Interest

def interest(p, r, t):
    si = (p * r * t) / 100
    ci = p * (1 + r / 100) ** t - p

    return si, ci

p = float(input("Enter principal amount: "))
r = float(input("Enter rate: "))
t = float(input("Enter time in years: "))

si, ci = interest(p, r, t)

print("Simple Interest:", si)
print("Compound Interest:", ci)


#22. Function to return all factors of a number

def factors(n):
    result = []

    for i in range(1, n + 1):
        if n % i == 0:
            result.append(i)

    return result

n = int(input("Enter a number: "))

if n > 0:
    print("Factors:", factors(n))
else:
    print("Enter a positive number")


#23. Function to find the second-largest number in a list

def second_largest(lst):
    largest = float('-inf')
    second = float('-inf')

    for i in lst:
        if i > largest:
            second = largest
            largest = i

        elif i > second and i != largest:
            second = i

    if second == float('-inf'):
        return "No second largest element"

    return second

numbers = [10, 20, 40, 30, 50]
print("Second Largest:", second_largest(numbers))


#24. Merge two lists without duplicates

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

result = []

for i in list1 + list2:
    if i not in result:
        result.append(i)

print("Merged List:", result)


#25. Find second-largest and second-smallest elements

lst = [10, 20, 30, 40, 50]

unique = []

for i in lst:
    if i not in unique:
        unique.append(i)

unique.sort()

if len(unique) < 2:
    print("Not enough distinct elements")
else:
    print("Second Smallest:", unique[1])
    print("Second Largest:", unique[-2])


#26. Rotate a list to the left by k positions

lst = [1, 2, 3, 4, 5]

k = int(input("Enter rotation value: "))

if len(lst) > 0:
    k = k % len(lst)
    result = lst[k:] + lst[:k]
    print("Rotated List:", result)
else:
    print("List is empty")


#27. Separate even and odd numbers into two lists

lst = [1, 2, 3, 4, 5, 6]

even = []
odd = []

for i in lst:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print("Even Numbers:", even)
print("Odd Numbers:", odd)


#28. Find common elements between two lists

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

common = []

for i in list1:
    if i in list2 and i not in common:
        common.append(i)

print("Common Elements:", common)


#29. Count frequency of each element in a tuple

t = (1, 2, 3, 2, 1, 4, 2)

freq = {}

for i in t:
    if i in freq:
        freq[i] = freq[i] + 1
    else:
        freq[i] = 1

print("Frequency:", freq)


#30. Find union, intersection and difference of two sets

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print("Union:", a | b)
print("Intersection:", a & b)
print("Difference:", a - b)


#31. Check whether one set is a subset of another

a = {1, 2}
b = {1, 2, 3, 4, 5}

if a.issubset(b):
    print("A is a subset of B")
else:
    print("A is not a subset of B")


#32. Count frequency of words in a sentence

sentence = input("Enter a sentence: ")

words = sentence.lower().split()

freq = {}

for i in words:
    if i in freq:
        freq[i] = freq[i] + 1
    else:
        freq[i] = 1

print("Word Frequency:", freq)


#33. Create a dictionary from two lists

keys = ["Name", "Age", "City"]
values = ["Trupti", 20, "Nashik"]

data = dict(zip(keys, values))

print(data)


#34. Sort a dictionary by its values

data = {"A": 30, "B": 10, "C": 20}

result = dict(sorted(data.items(), key=lambda x: x[1]))

print("Sorted Dictionary:", result)


#35. Read a text file and count lines, words and characters

file = open("sample.txt", "r")

data = file.read()

lines = data.splitlines()
words = data.split()
characters = len(data)

print("Number of Lines:", len(lines))
print("Number of Words:", len(words))
print("Number of Characters:", characters)

file.close()


#36. Copy only even-numbered lines from one file to another

source = open("input.txt", "r")
destination = open("output.txt", "w")

for i, line in enumerate(source, start=1):
    if i % 2 == 0:
        destination.write(line)

source.close()
destination.close()

print("Even-numbered lines copied successfully")


#37. Handle invalid integer input using try-except

try:
    n = int(input("Enter an integer: "))
    print("Number:", n)

except ValueError:
    print("Invalid input! Please enter an integer.")


#38. Handle file-not-found error while reading a file

try:
    file = open("sample.txt", "r")
    data = file.read()

    print(data)

    file.close()

except FileNotFoundError:
    print("File not found!")


#39. Create a random password generator

import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation

    password = ""

    for i in range(length):
        password = password + random.choice(characters)

    return password

length = int(input("Enter password length: "))

if length > 0:
    print("Generated Password:", generate_password(length))
else:
    print("Invalid password length")


#40. Calculate number of days between two dates

from datetime import datetime

date1 = input("Enter first date (DD-MM-YYYY): ")
date2 = input("Enter second date (DD-MM-YYYY): ")

d1 = datetime.strptime(date1, "%d-%m-%Y")
d2 = datetime.strptime(date2, "%d-%m-%Y")

difference = abs((d2 - d1).days)

print("Number of Days:", difference)