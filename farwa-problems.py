def problem_1():

    # ADD TWO NUMBERS
    num1 = float(input("Enter your first number"))
    num2 = float(input("Enter your second number"))

    result = num1 + num2
    print("the sum of", num1, "and", num2, "is", result)


def problem_2():

    # GET Quotient of two numbers
    number1 = float(input("Enter your first number"))
    number2 = float(input("Enter your second number"))
    result = number1 / number2
    result2 = number1 // number2
    print("the quotient of", number1, "and", number2, "is", result)
    print("the quotient of", number1, "and", number2, "is", result2)


def problem_3():

    # GET quotient and division of two numbers
    numerator = 20
    denominator = 13

    quotient = numerator / denominator  # Using division operator (/)
    division = numerator // denominator  # Using floor division operator (//)

    print("Quotient:", quotient)
    print("Division:", division)


def problem_4():

    # input four numbers and generate the sum of these

    num1 = float(input("Enter your first number"))
    num2 = float(input("enter your second number"))
    num3 = float(input("enter your third number"))
    num4 = float(input("enter your fourth number"))

    sum_of_numbers = num1 + num2 + num3 + num4
    print("The sum of numbers are", sum_of_numbers)


def problem_5():

    # Sum and average of marks of five students taken from the user
    num_students = 5
    total_marks = 0

    for i in range(num_students):
        marks = float(input("Enter the marks of student {}: ".format(i + 1)))
        total_marks += marks

    average_marks = total_marks / num_students

    print("Sum of marks:", total_marks)
    print("Average marks:", average_marks)


def problem_6():

    # percentage of total marks of four
    num_students = 4
    max_marks = 100
    total_marks = 0

    # Input marks for each student
    for i in range(num_students):
        marks = float(input("Enter the marks of student {}: ".format(i + 1)))
        total_marks += marks

    # Calculate percentage
    for i in range(num_students):
        marks = float(input("Enter the marks of student {}: ".format(i + 1)))
        percentage = (marks / max_marks) * 100
        print("Percentage of student {}: {:.2f}%".format(i + 1, percentage))


def problem_7():

    # check is number is greater than 80
    number = float(input("Enter a number"))
    if number > 80:
        print("Good")
    else:
        print("Try again")


def problem_8():

    # Get the number to check for divisibility
    number = int(input("Enter the number to check: "))

    # Get the number to divide by
    divisor = int(input("Enter the divisor: "))

    # Check for divisibility
    if number % divisor == 0:
        print(f"{number} is divisible by {divisor}.")
    else:
        print(f"{number} is not divisible by {divisor}.")


def problem_9():

    # Initialize a variable to hold the sum of odd numbers
    odd_sum = 0

    # Get 10 numbers from the user
    for i in range(10):
        number = int(input(f"Enter number {i + 1}: "))

        # Check if the number is odd
        if number % 2 != 0:
            odd_sum += number

    # Print the sum of odd numbers
    print("Sum of odd numbers:", odd_sum)


def problem_10():

    even_sum = 0

    # Get the value of n from the user
    n = int(input("Enter the value of n: "))

    # Get n numbers from the user
    for i in range(n):
        number = int(input(f"Enter number {i + 1}: "))

        # Check if the number is even
        if number % 2 == 0:
            even_sum += number

    # Print the sum of even numbers
    print("Sum of even numbers:", even_sum)


def problem_11():
    def fibonacci_series(n):
        series = [0, 1]  # Initialize the series with the first two terms

        for i in range(2, n):
            next_term = series[i - 1] + series[i - 2]
            series.append(next_term)

        return series[:n]  # Return only the first n terms

    # Example usage
    n = 10
    fibonacci_terms = fibonacci_series(n)
    print(fibonacci_terms)


def problem_12():
    def fahrenheit_to_celsius(fahrenheit):
        celsius = (fahrenheit - 32) * (5 / 9)
        return celsius

    # Example usage
    fahrenheit = int(input("Enter fahrenheit :"))
    celsius = fahrenheit_to_celsius(fahrenheit)
    print(celsius)


def problem_13():
    def calculate_pay(hours_worked, rate_per_hour):
        if hours_worked <= 40:
            pay = hours_worked * rate_per_hour
        else:
            overtime_hours = hours_worked - 40
            overtime_rate = rate_per_hour * 1.5
            pay = (40 * rate_per_hour) + (overtime_hours * overtime_rate)
        return pay

    # Example usage
    hours = int(input("Enter work hours :"))
    rate = 10000
    total_pay = calculate_pay(hours, rate)
    print("Your total pay is ", total_pay, "PKR")


def problem_14():
    def determine_status(marks, passing_marks):
        if marks >= passing_marks:
            status = "Pass"
        else:
            status = "Fail"
        return status

    marks_obtained = int(input("Enter your marks :"))
    passing_marks = 50
    student_status = determine_status(marks_obtained, passing_marks)
    print(student_status)


def problem_15():

    def determine_largest_number(num1, num2):
        if num1 > num2:
            largest_num = num1
        else:
            largest_num = num2
        return largest_num

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    largest_number = determine_largest_number(num1, num2)
    print("The largest number is:", largest_number)


#take three numbers from the user and determine the largest
def problem_16():
    def determine_largest_number(num1, num2, num3):
        largest_num = max(num1, num2, num3)
        return largest_num

    # Example usage
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    num3 = float(input("Enter the third number: "))
    largest_number = determine_largest_number(num1, num2, num3)
    print("The largest number is:", largest_number)


# using nested if-else
def problem_17():
    def determine_largest_number_nested(num1, num2, num3, num4):
        largest_num = num1

        if num2 > largest_num:
            largest_num = num2

        if num3 > largest_num:
            largest_num = num3

        if num4 > largest_num:
            largest_num = num4

        return largest_num

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    num3 = float(input("Enter the third number: "))
    num4 = float(input("Enter the third number: "))
    largest_number_nested = determine_largest_number_nested(num1, num2, num3, num4)
    print("Largest number using nested if-else:", largest_number_nested)


#using compound composition
def problem_18():
        def determine_largest_number_compound(num1, num2, num3, num4):
            largest_num = max(num1, num2, num3, num4)
            return largest_num

        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        num3 = float(input("Enter the third number: "))
        num4 = float(input("Enter the third number: "))
        largest_number_compound = determine_largest_number_compound(num1, num2, num3, num4)
        print("Largest number using compound conditions:", largest_number_compound)


#using third approach
def problem_19():
    # Approach 3: Calling the first number the largest and revising estimate
    def determine_largest_number_estimate(num1, num2, num3, num4):
        largest_num = num1

        if num2 > largest_num:
            largest_num = num2

        if num3 > largest_num:
            largest_num = num3

        if num4 > largest_num:
            largest_num = num4

        return largest_num

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    num3 = float(input("Enter the third number: "))
    num4 = float(input("Enter the third number: "))
    largest_number_estimate = determine_largest_number_estimate(num1, num2, num3, num4)
    print("Largest number using estimation approach:", largest_number_estimate)


def problem_20():
    def calculate_grade(marks):
        if marks >= 90 and marks <= 100:
         return "A"
        elif marks >= 80 and marks <= 89:
         return "B"
        elif marks >= 70 and marks <= 79:
         return "C"
        elif marks >= 60 and marks <= 69:
         return "D"
        else:
         return "F"

    student_marks = float(input("Enter your marks :"))
    student_grade = calculate_grade(student_marks)
    print("Student Grade:", student_grade)


def problem_21():
    def check_even_odd(number):
        if number % 2 == 0:
            return "Even"
        else:
            return "Odd"

    # Example usage:
    user_number = int(input("Enter a number: "))
    result = check_even_odd(user_number)
    print("The number is", result)


def problem_22():
    from datetime import datetime, timedelta

    def calculate_time_difference(time1, time2):
        fmt = '%H:%M'
        datetime1 = datetime.strptime(time1, fmt)
        datetime2 = datetime.strptime(time2, fmt)
        difference = datetime2 - datetime1
        return difference

    time1 = "10:15"
    time2 = "13:45"

    time_difference = calculate_time_difference(time1, time2)
    print("Time difference:", time_difference)


def problem_23():
    def check_numbers(a, b, c):
        if a == b == c:
            return "All numbers are the same"
        elif a != b and b != c and a != c:
            return "All numbers are different"
        else:
            return "Exactly two numbers are the same"

    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    num3 = int(input("Enter the third number: "))
    result = check_numbers(num1, num2, num3)
    print(result)


def problem_24():
    sum = 0

    for i in range(10):
        num = float(input("Enter number {}: ".format(i + 1)))
        sum += num
    print("The sum of the 10 numbers is:", sum)


def problem_25():
    n = int(input("Enter the count of numbers: "))
    sum = 0

    for i in range(n):
        num = float(input("Enter number {}: ".format(i + 1)))
        sum += num
    print("The sum of the", n, "numbers is:", sum)


def problem_26():
    n = int(input("Enter the count of numbers: "))
    sum = 0
    for i in range(n):
        num = float(input("Enter number {}: ".format(i + 1)))
        sum += num
    average = sum / n
    print("The average of the", n, "numbers is:", average)


def problem_27():
    n = int(input("Enter a number: "))
    for i in range(1, n + 1):
        print(i)


def problem_28():
    n = int(input("Enter a positive integer: "))
    if n < 0:
        print("Error: Please enter a positive integer.")
    elif n == 0:
        factorial = 1
    else:
        factorial = 1
        for i in range(1, n + 1):
            factorial *= i

    print("The factorial of", n, "is", factorial)


def problem_29():
    a = int(input("Enter the value of 'a': "))
    n = int(input("Enter the value of 'n': "))

    result = 1
    for _ in range(n):
        result *= a

    print(f"The result of {a} raised to the power of {n} is: {result}")


def problem_30():
    numbers = []

    for i in range(3):
        num = int(input(f"Enter number {i + 1}: "))
        numbers.append(num)

    largest = numbers[0]

    for num in numbers:
        if num > largest:
            largest = num

    print(f"The largest number is: {largest}")


def problem_31():
    n = int(input("Enter a value of n :"))
    numbers = []

    for i in range(n):
        num = int(input(f"Enter number {i + 1}: "))
        numbers.append(num)

    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    print(f"The largest number is: {largest}")


def problem_32():
    n = int(input("Enter the value of 'n': "))

    numbers = []

    for i in range(n):
        num = int(input(f"Enter number {i + 1}: "))
        numbers.append(num)

    smallest = numbers[0]
    largest = numbers[0]
    for num in numbers:
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num

    print(f"The smallest number is: {smallest}")
    print(f"The largest number is: {largest}")


def problem_33():
    n = int(input("Enter the value of 'n': "))

    positive_count = 0
    negative_count = 0

    for i in range(n):
        num = int(input(f"Enter number {i + 1}: "))
        if num > 0:
            positive_count += 1
        elif num < 0:
            negative_count += 1

    print(f"Number of positive integers: {positive_count}")
    print(f"Number of negative integers: {negative_count}")


def problem_34():
    n = int(input("Enter a positive integer: "))

    divisors = []

    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)

    print(f"The divisors of {n} are: {divisors}")


def problem_35():
    n = int(input("Enter a positive integer: "))

    divisors_sum = 0

    for i in range(1, n):
        if n % i == 0:
            divisors_sum += i

    if divisors_sum == n:
        print(f"{n} is a perfect number.")
    else:
        print(f"{n} is not a perfect number.")


if __name__ == "__main__":

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
    # problem_21()
    # problem_22()
    # problem_23()
    # problem_24()
    # problem_25()
    # problem_26()
    # problem_27()
    # problem_28()
    # problem_29()
    # problem_30()
    # problem_31()
    # problem_32()
    # problem_33()
    # problem_34()
    problem_35()