#1. Check whether a number is positive, negative, or zero


num = int(input("Enter a number: "))

if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")





#2. Check whether a number is even or odd

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")





#3. Find the greater of two numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("First number is greater")
elif b > a:
    print("Second number is greater")
else:
    print("Both numbers are equal")







#4. Find the greatest of three numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Greatest number is", a)
elif b >= a and b >= c:
    print("Greatest number is", b)
else:
    print("Greatest number is", c)






#5. Check voting eligibility (age 18 or above)

age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")





#6. Check whether a year is a leap year

year = int(input("Enter a year: "))

if year % 400 == 0:
    print("Leap year")
elif year % 100 == 0:
    print("Not a leap year")
elif year % 4 == 0:
    print("Leap year")
else:
    print("Not a leap year")






#7. Check whether a character is a vowel or consonant

ch = input("Enter a character: ").lower()

if ch in "aeiou" and len(ch) == 1:
    print("Vowel")
elif ch.isalpha() and len(ch) == 1:
    print("Consonant")
else:
    print("Enter a single alphabet")






#8. Check whether a number is divisible by 5 and 11

num = int(input("Enter a number: "))

if num % 5 == 0 and num % 11 == 0:
    print("Number is divisible by 5 and 11")
else:
    print("Number is not divisible by both 5 and 11")






#9. Check whether a number is a multiple of both 3 and 7

num = int(input("Enter a number: "))

if num % 3 == 0 and num % 7 == 0:
    print("Multiple of 3 and 7")
else:
    print("Not a multiple of both 3 and 7")






#10. Assign grades based on marks

marks = int(input("Enter marks: "))

if marks < 0 or marks > 100:
    print("Invalid marks")
elif marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
elif marks >= 60:
    print("Grade D")
else:
    print("Grade F")






#11. Check whether a character is uppercase or lowercase

ch = input("Enter a character: ")

if len(ch) != 1 or not ch.isalpha():
    print("Enter a single alphabet")
elif ch.isupper():
    print("Uppercase letter")
else:
    print("Lowercase letter")






#12. Check whether an entered alphabet is a vowel using if-elif

ch = input("Enter an alphabet: ").lower()

if ch == 'a':
    print("Vowel")
elif ch == 'e':
    print("Vowel")
elif ch == 'i':
    print("Vowel")
elif ch == 'o':
    print("Vowel")
elif ch == 'u':
    print("Vowel")
else:
    print("Consonant")





#13. Check whether three sides can form a triangle

a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

if a <= 0 or b <= 0 or c <= 0:
    print("Invalid sides")
elif a + b > c and a + c > b and b + c > a:
    print("Triangle can be formed")
else:
    print("Triangle cannot be formed")






#14. Determine the type of triangle

a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

if a <= 0 or b <= 0 or c <= 0:
    print("Invalid sides")
elif a + b <= c or a + c <= b or b + c <= a:
    print("Triangle cannot be formed")
elif a == b and b == c:
    print("Equilateral triangle")
elif a == b or b == c or a == c:
    print("Isosceles triangle")
else:
    print("Scalene triangle")






#15. Find the largest among four numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))

if a >= b and a >= c and a >= d:
    print("Largest number is", a)
elif b >= a and b >= c and b >= d:
    print("Largest number is", b)
elif c >= a and c >= b and c >= d:
    print("Largest number is", c)
else:
    print("Largest number is", d)





#16. Check whether a number is a three-digit number

num = int(input("Enter a number: "))

if 100 <= abs(num) <= 999:
    print("Three-digit number")
else:
    print("Not a three-digit number")






#17. Calculate electricity bill using slab rates

units = float(input("Enter electricity units: "))

if units < 0:
    print("Invalid units")
elif units <= 100:
    bill = units * 5
    print("Electricity bill: Rs.", bill)
elif units <= 200:
    bill = 100 * 5 + (units - 100) * 7
    print("Electricity bill: Rs.", bill)
else:
    bill = 100 * 5 + 100 * 7 + (units - 200) * 10
    print("Electricity bill: Rs.", bill)







#18. Calculate income tax based on income slabs

income = float(input("Enter annual income: "))

if income < 0:
    print("Invalid income")
elif income <= 250000:
    tax = 0
elif income <= 500000:
    tax = (income - 250000) * 0.05
elif income <= 1000000:
    tax = 12500 + (income - 500000) * 0.20
else:
    tax = 112500 + (income - 1000000) * 0.30

if income >= 0:
    print("Income tax: Rs.", tax)






#19. Check whether a student passes

m1 = int(input("Enter marks in subject 1: "))
m2 = int(input("Enter marks in subject 2: "))
m3 = int(input("Enter marks in subject 3: "))

if m1 >= 35 and m2 >= 35 and m3 >= 35:
    print("Student passed")
else:
    print("Student failed")






#20. Check whether a number is within a given range

num = int(input("Enter a number: "))
low = int(input("Enter lower limit: "))
high = int(input("Enter upper limit: "))

if low > high:
    print("Invalid range")
elif low <= num <= high:
    print("Number is within the range")
else:
    print("Number is outside the range")







#21. Build a simple calculator using if-elif-else

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

if op == '+':
    print("Result:", a + b)
elif op == '-':
    print("Result:", a - b)
elif op == '*':
    print("Result:", a * b)
elif op == '/':
    if b != 0:
        print("Result:", a / b)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operator")







#22. Check whether a year is a century leap year

year = int(input("Enter a year: "))

if year % 100 == 0 and year % 400 == 0:
    print("Century leap year")
elif year % 100 == 0:
    print("Century year but not a leap year")
elif year % 4 == 0:
    print("Leap year but not a century year")
else:
    print("Not a leap year")






#23. Determine the season based on the month number

month = int(input("Enter month number (1-12): "))

if month < 1 or month > 12:
    print("Invalid month")
elif month == 12 or month == 1 or month == 2:
    print("Winter")
elif month >= 3 and month <= 5:
    print("Summer")
elif month >= 6 and month <= 9:
    print("Monsoon")
else:
    print("Post-monsoon")






#24. Find the number of days in a month

month = int(input("Enter month number (1-12): "))
year = int(input("Enter year: "))

if month < 1 or month > 12:
    print("Invalid month")
elif month == 2:
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        print("29 days")
    else:
        print("28 days")
elif month == 4 or month == 6 or month == 9 or month == 11:
    print("30 days")
else:
    print("31 days")







#25. Check whether a password meets minimum conditions

password = input("Enter password: ")

has_digit = False
has_letter = False

for ch in password:
    if ch.isdigit():
        has_digit = True
    elif ch.isalpha():
        has_letter = True

if len(password) < 8:
    print("Password must contain at least 8 characters")
elif not has_digit:
    print("Password must contain at least one digit")
elif not has_letter:
    print("Password must contain at least one alphabet")
else:
    print("Password meets the conditions")








#26. Determine ticket price based on age category

age = int(input("Enter your age: "))

if age < 0:
    print("Invalid age")
elif age < 5:
    print("Ticket is free")
elif age <= 17:
    print("Ticket price: Rs. 100")
elif age <= 59:
    print("Ticket price: Rs. 200")
else:
    print("Ticket price: Rs. 120")







#27. Calculate discount based on purchase amount

amount = float(input("Enter purchase amount: "))

if amount < 0:
    print("Invalid amount")
elif amount < 1000:
    discount = 0
elif amount < 5000:
    discount = amount * 0.05
elif amount < 10000:
    discount = amount * 0.10
else:
    discount = amount * 0.15

if amount >= 0:
    print("Discount: Rs.", discount)
    print("Final amount: Rs.", amount - discount)







#28. Check eligibility for a driving licence

age = int(input("Enter your age: "))
eyesight = input("Is eyesight satisfactory? (yes/no): ").lower()

if age < 18:
    print("Not eligible due to age")
elif eyesight != "yes":
    print("Not eligible due to eyesight condition")
else:
    print("Eligible, subject to official requirements")







#29. Create a login system with username and password validation

correct_username = "admin"
correct_password = "12345"

username = input("Enter username: ")
password = input("Enter password: ")

if username == correct_username and password == correct_password:
    print("Login successful")
elif username != correct_username:
    print("Incorrect username")
else:
    print("Incorrect password")








#30. Create a menu-driven calculator

while True:
    print("\n1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '5':
        print("Exiting program")
        break
    elif choice in ['1', '2', '3', '4']:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if choice == '1':
            print("Result:", a + b)
        elif choice == '2':
            print("Result:", a - b)
        elif choice == '3':
            print("Result:", a * b)
        elif choice == '4':
            if b != 0:
                print("Result:", a / b)
            else:
                print("Cannot divide by zero")
    else:
        print("Invalid choice")
