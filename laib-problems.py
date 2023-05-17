def problem_1():
    pass
    # add two numbers
    a = 20
    b = 40
    total = a + b
    print(total)


def problem_2():
    # input 4 values
    a, b, c, d = 20, 2, 3, 4
    print(a + b + c + d)


def problem_3():
    # Input the two numbers
    numerator = float(input("Enter the numerator: "))
    denominator = float(input("Enter the denominator: "))

    # Calculate the quotient
    quotient = numerator / denominator

    # Print the quotient
    print("Quotient:", quotient)


def problem_4():
    # sum and avg of students
    # Initializes variables
    sum_marks = 0
    average_marks = 0

    # Get marks from user input
    marks = []
    for i in range(5):
        marks.append(float(input("Enter marks for student {}: ".format(i + 1))))
        sum_marks += marks[i]

    # Calculate average
    average_marks = sum_marks / len(marks)

    # Print results
    print("Sum of marks: ", sum_marks)
    print("Average of marks: ", average_marks)


def problem_5():
    # Get total marks of four students
    total_marks = []
    for i in range(4):
        marks = float(input(f"Enter total marks of student {i + 1}: "))
        total_marks.append(marks)

    # Calculate sum of total marks
    sum_marks = sum(total_marks)

    # Calculate percentage for each student
    for i, marks in enumerate(total_marks):
        percentage = (marks / sum_marks) * 100
        print(f"Percentage of total marks for student {i + 1}: {percentage:.2f}%")


def problem_6():
    pass
    number = float(input("enter a number:"))
    if number > 80:
        print("Good")
    else:
        print("try again")


def problem_7():
    number = int(input("Enter a number: "))
    divisor = int(input("Enter a divisor: "))

    if number % divisor == 0:
        print(f"{number} is divisible by {divisor}")
    else:
        print(f"{number} is not divisible by {divisor}")


def problem_8():
    sum_of_odd = 0

    for _ in range(10):
        number = int(input("Enter a number: "))
        if number % 2 != 0:
            sum_of_odd += number

    print("Sum of odd numbers:", sum_of_odd)


def problem_9():
    n = int(input("Enter the value of n: "))
    sum_of_even = 0

    for _ in range(n):
        number = int(input("Enter a number: "))
        if number % 2 == 0:
            sum_of_even += number

    print("Sum of even numbers:", sum_of_even)


def problem_10():
    n = int(input("Enter the number of terms: "))

    # First two terms of the Fibonacci series
    first_term = 0
    second_term = 1

    # Print the first n terms of the Fibonacci series
    print("Fibonacci Series:")
    print(first_term)  # Print the first term

    if n > 1:
        print(second_term)  # Print the second term

        # Generate and print the remaining terms
        for i in range(2, n):
            next_term = first_term + second_term
            print(next_term)
            first_term, second_term = second_term, next_term


def problem_11():
    # Get temperature in Fahrenheit from the user
    fahrenheit = float(input("Enter the temperature in Fahrenheit: "))

    # Convert Fahrenheit to Celsius
    celsius = (fahrenheit - 32) * (5 / 9)

    # Print the converted temperature in Celsius
    print("The temperature in Celsius is:", celsius)


def problem_12():
    # Get the number of hours worked and the rate per hour from the user
    hours_worked = float(input("Enter the number of hours worked: "))
    rate_per_hour = float(input("Enter the rate per hour: "))

    # Calculate the pay
    pay = hours_worked * rate_per_hour

    # Print the pay
    print("The employee's pay is:", pay)


def problem_13():
    # Get the marks from the user
    marks = float(input("Enter the marks: "))

    # Check if the marks are greater than or equal to the passing marks
    if marks >= 50:
        print("Pass")
    else:
        print("Fail")


def problem_14():
    # Get the input from the user
    hours_worked = float(input("Enter the total hours worked this week: "))
    hourly_rate = float(input("Enter the hourly pay rate: "))

    # Calculate the regular pay and overtime pay
    if hours_worked <= 40:
        regular_pay = hours_worked * hourly_rate
        overtime_pay = 0
    else:
        regular_pay = 40 * hourly_rate
        overtime_hours = hours_worked - 40
        overtime_pay = overtime_hours * (hourly_rate * 1.5)

    # Calculate the total pay for the week
    total_pay = regular_pay + overtime_pay

    # Output the results
    print("Regular Pay: $", regular_pay)
    print("Overtime Pay: $", overtime_pay)
    print("Total Pay for the Week: $", total_pay)


def problem_15():
    # Get the input from the user
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Compare the numbers and determine the largest
    if num1 > num2:
        largest_num = num1
    else:
        largest_num = num2

    # Output the largest number
    print("The largest number is:", largest_num)


def problem_16():
    # Get the marks obtained from the user
    marks = float(input("Enter the marks obtained: "))

    # Determine the grade based on the marks
    if marks >= 90:
        grade = "A"
    elif marks >= 80:
        grade = "B"
    elif marks >= 70:
        grade = "C"
    elif marks >= 60:
        grade = "D"
    else:
        grade = "F"

    # Output the grade
    print("Grade: ", grade)


def problem_17():
    number = int(input("Enter a number: "))

    # Check if the number is even or odd
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")


def problem_18():
    # Get the two time inputs from the user
    time1 = input("Enter the first time (hh:mm): ")
    time2 = input("Enter the second time (hh:mm): ")

    # Split the time inputs into hours and minutes
    hours1, minutes1 = time1.split(":")
    hours2, minutes2 = time2.split(":")

    # Convert the hours and minutes to integers
    hours1 = int(hours1)
    minutes1 = int(minutes1)
    hours2 = int(hours2)
    minutes2 = int(minutes2)

    # Calculate the total minutes for each time
    total_minutes1 = hours1 * 60 + minutes1
    total_minutes2 = hours2 * 60 + minutes2

    # Calculate the difference in minutes
    difference_minutes = total_minutes2 - total_minutes1

    # Convert the difference in minutes to hours and minutes
    difference_hours = difference_minutes // 60
    difference_minutes %= 60

    # Output the difference in hours and minutes
    print("The difference is:", difference_hours, "hours", difference_minutes, "minutes")


def problem_19():
    # input three nums
    # Get three numbers from the user
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    num3 = float(input("Enter the third number: "))

    # Check the relationship between the numbers
    if num1 == num2 == num3:
        print("All numbers are the same")
    elif num1 != num2 and num1 != num3 and num2 != num3:
        print("All numbers are different")
    else:
        print("Exactly two numbers are the same")


def problem_20():
    # Get the value of n from the user
    n = int(input("Enter the value of n: "))

    # Initialize the sum variable
    sum = 0

    # Use a loop to iterate n times
    for i in range(n):
        # Get a number from the user
        num = float(input("Enter a number: "))

        # Add the number to the sum
        sum += num

    # Print the sum
    print("The sum is:", sum)


def problem_21():
    # Get the value of n from the user
    n = int(input("Enter the value of n: "))

    # Initialize the sum variable
    sum = 0

    # Use a loop to iterate n times
    for i in range(n):
        # Get a number from the user
        num = float(input("Enter a number: "))

        # Add the number to the sum
        sum += num

    # Print the sum
    print("The sum is:", sum)

if __name__ == '__main__':
    # problem_1()
    # problem_2()
    # problem_3()
    # problem_4()
    # problem_5()
    # problem_6()
    # problem_7()
    # problem_8()
    # problem_9()
    # problem_10()
    # problem_11()
    # problem_12()
    # problem_13()
    # problem_14()
    # problem_15()
    # problem_16()
    # problem_17()
    # problem_18()
    # problem_19()
    # problem_20()
    problem_21()


