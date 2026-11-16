
#1. Check whether a number is even or odd

n = int(input("Enter a number: "))

if n % 2 == 0:
    print("Even number")
else:
    print("Odd number")


#2. Find the largest of three numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest number:", a)
elif b >= a and b >= c:
    print("Largest number:", b)
else:
    print("Largest number:", c)


#3. Check whether a given number is prime

n = int(input("Enter a number: "))

if n <= 1:
    print("Not a prime number")
else:
    for i in range(2, n):
        if n % i == 0:
            print("Not a prime number")
            break
    else:
        print("Prime number")


#4. Print the Fibonacci series up to n terms

n = int(input("Enter number of terms: "))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b


#5. Find the factorial of a number using a loop

n = int(input("Enter a number: "))

fact = 1

for i in range(1, n + 1):
    fact = fact * i

print("Factorial:", fact)


#6. Reverse a string without using [::-1]

s = input("Enter a string: ")

rev = ""

for i in s:
    rev = i + rev

print("Reversed string:", rev)


#7. Check whether a string is a palindrome

s = input("Enter a string: ")

rev = ""

for i in s:
    rev = i + rev

if s == rev:
    print("Palindrome")
else:
    print("Not a palindrome")


#8. Count the number of vowels and consonants in a string

s = input("Enter a string: ")

vowels = 0
consonants = 0

for i in s:
    if i.isalpha():
        if i.lower() in "aeiou":
            vowels += 1
        else:
            consonants += 1

print("Vowels:", vowels)
print("Consonants:", consonants)


#9. Find the sum of all elements in a list

lst = [10, 20, 30, 40, 50]

total = 0

for i in lst:
    total = total + i

print("Sum of elements:", total)


#10. Find the largest and smallest element in a list without using max() or min()

lst = [10, 25, 5, 40, 15]

largest = lst[0]
smallest = lst[0]

for i in lst:
    if i > largest:
        largest = i

    if i < smallest:
        smallest = i

print("Largest element:", largest)
print("Smallest element:", smallest)


#11. Remove duplicate elements from a list

lst = [10, 20, 30, 10, 20, 40, 50]

new_list = []

for i in lst:
    if i not in new_list:
        new_list.append(i)

print("List after removing duplicates:", new_list)


#12. Count how many times each element appears in a list using a dictionary

lst = [10, 20, 10, 30, 20, 10, 40]

freq = {}

for i in lst:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

print("Frequency:", freq)


#13. Find the second-largest number in a list

lst = [10, 20, 40, 30, 50]

largest = lst[0]
second = None

for i in lst:
    if i > largest:
        second = largest
        largest = i
    elif i != largest and (second is None or i > second):
        second = i

print("Second largest number:", second)


#14. Sort a list without using sort() or sorted()

lst = [40, 10, 50, 20, 30]

for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i] > lst[j]:
            lst[i], lst[j] = lst[j], lst[i]

print("Sorted list:", lst)


#15. Write a function that accepts a list and returns only even numbers

def even_numbers(lst):
    result = []

    for i in lst:
        if i % 2 == 0:
            result.append(i)

    return result


lst = [10, 15, 20, 25, 30, 35]

print("Even numbers:", even_numbers(lst))


#16. Find the frequency of each character in a string

s = input("Enter a string: ")

freq = {}

for i in s:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

print("Character frequency:", freq)


#17. Check whether two strings are anagrams of each other

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

s1 = s1.lower().replace(" ", "")
s2 = s2.lower().replace(" ", "")

if sorted(s1) == sorted(s2):
    print("Anagrams")
else:
    print("Not Anagrams")


#18. Find all duplicate values in a list

lst = [10, 20, 30, 10, 40, 20, 50]

duplicates = []

for i in lst:
    if lst.count(i) > 1 and i not in duplicates:
        duplicates.append(i)

print("Duplicate values:", duplicates)


#19. Find the longest word in a sentence

s = input("Enter a sentence: ")

words = s.split()

longest = ""

for i in words:
    if len(i) > len(longest):
        longest = i

print("Longest word:", longest)


#20. Student marks program - Calculate total, percentage, grade and pass/fail

marks = []

for i in range(5):
    m = int(input("Enter marks: "))
    marks.append(m)

total = sum(marks)

percentage = total / 5

print("Total marks:", total)
print("Percentage:", percentage, "%")

if any(m < 35 for m in marks):
    print("Result: Fail")
    print("Grade: F")
elif percentage >= 90:
    print("Grade: A")
    print("Result: Pass")
elif percentage >= 75:
    print("Grade: B")
    print("Result: Pass")
elif percentage >= 60:
    print("Grade: C")
    print("Result: Pass")
else:
    print("Grade: D")
    print("Result: Pass")
