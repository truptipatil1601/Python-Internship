#1. Check whether a number is Even or Odd

def is_even(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

num = int(input("Enter a number: "))
print(is_even(num))


#2. Find the Largest of Two Numbers

def largest(a, b):
    if a > b:
        return a
    else:
        return b

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Largest number:", largest(a, b))


#3. Print Numbers from 1 to n

def print_numbers(n):
    for i in range(1, n + 1):
        print(i)

n = int(input("Enter a number: "))
print_numbers(n)


#4. Find the Sum of Numbers from 1 to n

def sum_n(n):
    total = 0

    for i in range(1, n + 1):
        total = total + i

    return total

n = int(input("Enter a number: "))
print("Sum:", sum_n(n))


#5. Print Multiplication Table

def table(n):
    for i in range(1, 11):
        print(n, "x", i, "=", n * i)

n = int(input("Enter a number: "))
table(n)


#6. Count Even Numbers in a List

def count_even(lst):
    count = 0

    for i in lst:
        if i % 2 == 0:
            count = count + 1

    return count

numbers = [1, 2, 3, 4, 6]
print("Even numbers count:", count_even(numbers))


#7. Find Maximum Number Without Using max()

def find_max(lst):
    largest = lst[0]

    for i in lst:
        if i > largest:
            largest = i

    return largest

numbers = [10, 25, 5, 40, 15]
print("Largest number:", find_max(numbers))


#8. FizzBuzz (Print Numbers from 1 to 100)

def fizzbuzz():
    for i in range(1, 101):

        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")

        elif i % 3 == 0:
            print("Fizz")

        elif i % 5 == 0:
            print("Buzz")

        else:
            print(i)

fizzbuzz()


#9. Check Whether a String is Palindrome

def palindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False

word = input("Enter a string: ")
print(palindrome(word))


#10. Count Vowels in a String

def count_vowels(s):
    count = 0

    for i in s:
        if i in "aeiouAEIOU":
            count = count + 1

    return count

word = input("Enter a string: ")
print("Number of vowels:", count_vowels(word))


#11. Find Second Largest Number Without Using sort()

def second_largest(lst):
    largest = float('-inf')
    second = float('-inf')

    for i in lst:
        if i > largest:
            second = largest
            largest = i

        elif i > second and i != largest:
            second = i

    return second

numbers = [10, 20, 40, 30, 50]
print("Second largest:", second_largest(numbers))


#12. Number Guessing Game

import random

def guessing_game():
    number = random.randint(1, 10)

    while True:
        guess = int(input("Guess a number between 1 and 10: "))

        if guess == number:
            print("Correct Guess!")
            break

        elif guess < number:
            print("Too Low!")

        else:
            print("Too High!")

guessing_game()


#13. Assign Grade According to Marks

def grade(marks):
    if marks >= 90:
        return "A"

    elif marks >= 80:
        return "B"

    elif marks >= 70:
        return "C"

    elif marks >= 60:
        return "D"

    else:
        return "F"

marks = int(input("Enter your marks: "))
print("Grade:", grade(marks))
```

