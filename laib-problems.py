def problem_1():
    # Add two numbers
    a = 20
    b = 40
    total = a + b
    print(total)


def problem_2():
    # Input 4 values
    a, b, c, d = 20, 2, 3, 4
    print(a + b + c + d)


def problem_3():
    # Get quotient of division of two numbers
    # Input the two numbers
    numerator = float(input("Enter the numerator: "))
    denominator = float(input("Enter the denominator: "))

    # Calculate the quotient
    quotient = numerator / denominator

    # Print the quotient
    print("Quotient:", quotient)


def problem_4_sum_and_average():
    # Sum and average of marks of five students taken from the user
    # sum and avg of students
    # Initializes variables
    sum_marks = 0
    average_marks = 0
    #fixme take total marks from user as well

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
    # Sum and average of marks of five students taken from the user
    # Get total marks of four students
    total_marks = []
    for i in range(4):
        marks = float(input(f"Enter total marks of student {i + 1}: "))
        total_marks.append(marks)

    # Calculate sum of total marks
    sum_marks = sum(total_marks)
    percentage = (marks / sum_marks) * 100

    # Calculate percentage for each student
    # for i, marks in enumerate(total_marks):
    #     percentage = (marks / sum_marks) * 100
    #     print(f"Percentage of total marks for student {i + 1}: {percentage:.2f}%")


def print() -> object:
    pass


def problem_6():
    #  Check if a number is greater than 80, say “good”, if not say, “Try again”
    # enter a num to calculate percentage
    number = float(input("enter a number:"))
    if number > 80:
        print("Good")
    else:
        print("try again")


def problem_7():
    #Check whether a number is divisible by another user-given number or not
    number = int(input("Enter a number: "))
    divisor = int(input("Enter a divisor: "))

    if number % divisor == 0:
        print(f"{number} is divisible by {divisor}")
    else:
        print(f"{number} is not divisible by {divisor}")


def problem_8():
    # um of odd numbers from 10 user-given numbers
    # sum of odd num
    sum_of_odd = 0

    for _ in range(10):
        number = int(input("Enter a number: "))
        if number % 2 != 0:
            sum_of_odd += number

    print("Sum of odd numbers:", sum_of_odd)


def problem_9():
    # Sum of even number from n user-given numbers. Where n is also user-input.
    # sum of even num
    n = int(input("Enter the value of n: "))
    sum_of_even = 0

    for _ in range(n):
        number = int(input("Enter a number: "))
        if number % 2 == 0:
            sum_of_even += number

    print("Sum of even numbers:", sum_of_even)


def problem_10():
    # Show first n terms of Fibonacci serie
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
    # Converting temperature from Fahrenheit to Celsius [Formula: C = (f-32) * (5/9)]
    # Get temperature in Fahrenheit from the user
    fahrenheit = float(input("Enter the temperature in Fahrenheit: "))

    # Convert Fahrenheit to Celsius
    celsius = (fahrenheit - 32) * (5 / 9)

    # Print the converted temperature in Celsius
    print("The temperature in Celsius is:", celsius)


def problem_12():
    # Calculating pay for an employee, given the hours worked and rate per hour
    # Get the number of hours worked and the rate per hour from the user
    hours_worked = float(input("Enter the number of hours worked: "))
    rate_per_hour = float(input("Enter the rate per hour: "))

    # Calculate the pay
    pay = hours_worked * rate_per_hour

    # Print the pay
    print("The employee's pay is:", pay)


def problem_13():
    #  Determine the status of a student (pass or fail) given his/her marks in a subject
    # (passing marks = 50)
    # Get the marks from the user
    marks = float(input("Enter the marks: "))

    # Check if the marks are greater than or equal to the passing marks
    if marks >= 50:
        print("Pass")
    else:
        print("Fail")


def problem_14():
    #  Calculate pay of an employee based on the hours worked. The input includes the
    # employee total hours worked this week and their hourly pay rate. The employee is
    # to be paid their basic wage for the first 40 hours and time-and-a-half (i.e. 50%
    # more) for all hours above 40 (overtime pay). Output the regular pay. Overtime pay
    # and total pay for the week on the screen. If the employee worked 40 hours or less,
    # don’t output any information about overtime pay.
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
    # Take two number from the user and determine the largest number
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
    #  Determine the grade of a student from the marks obtained (90-100, A; 80-29, B;
    # 70-79, C; 60-69, D; <60, F)
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
    # Input a number and determine whether the number is even or odd
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
    # Input 3 numbers. Determine whether: all are same, all are different or exactly two
    # are same.
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
    #
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


def problem_22():
    # Displaying positive integers in the range from 1 to n, where n is taken from the user
    n = int(input("Enter a number: "))

    # Display positive integers from 1 to n
    for i in range(1, n + 1):
        print(i)


def problem_23():
    #  Calculate the factorial of a positive integer entered by the user
    n = int(input("Enter a positive integer: "))

    # Initialize the factorial variable
    factorial = 1

    # Calculate the factorial
    for i in range(1, n + 1):
        factorial *= i

    # Display the factorial
    print("The factorial of", n, "is", factorial)


def problem_24():
    # Take three number from the user and determine the largest number. Do it using a
    # loop
    numbers = []

    # Take three numbers from the user
    for i in range(3):
        num = int(input("Enter a number: "))
        numbers.append(num)

    # Initialize the largest number as the first number
    largest = numbers[0]

    # Find the largest number
    for num in numbers:
        if num > largest:
            largest = num

    # Display the largest number
    print("The largest number is:", largest)


def problem_25():
    #
    n = int(input("Enter the number of elements: "))

    # Initialize the largest number as None
    largest = None

    # Take n numbers from the user
    for i in range(n):
        num = int(input("Enter a number: "))
        if largest is None or num > largest:
            largest = num

    # Display the largest number
    print("The largest number is:", largest)


def problem_26():
    # Take n numbers from the user and determine both the smallest and the largest
    # number entered by the user, where n is taken from the user as well.
    n = int(input("Enter the number of elements: "))

    # Initialize the smallest and largest numbers as None
    smallest = None
    largest = None

    # Take n numbers from the user
    for i in range(n):
        num = int(input("Enter a number: "))
        if smallest is None or num < smallest:
            smallest = num
        if largest is None or num > largest:
            largest = num

    # Display the smallest and largest numbers
    print("The smallest number is:", smallest)
    print("The largest number is:", largest)


def problem_27():
    # Take n numbers from the user and determine that how many positive and negative
    # integers were entered by the user.
    n = int(input("Enter the number of elements: "))

    positive_count = 0
    negative_count = 0

    for i in range(n):
        num = int(input("Enter a number: "))
        if num > 0:
            positive_count += 1
        elif num < 0:
            negative_count += 1

    print("Number of positive integers:", positive_count)
    print("Number of negative integers:", negative_count)


def problem_28():
    n = int(input("Enter a positive integer: "))

    print("Divisors of", n, ":")

    for i in range(1, n + 1):
        if n % i == 0:
            print(i)


def problem_29():
    #   Take n numbers from the user and determine that how many positive and negative
    # integers were entered by the user.
    n = int(input("Enter a positive integer: "))

    divisors_sum = 0

    for i in range(1, n):
        if n % i == 0:
            divisors_sum += i

    if divisors_sum == n:
        print(n, "is a perfect number.")
    else:
        print(n, "is not a perfect number.")


def problem_30():
    # Input a positive integer from the user and determine whether is a prime number or
    # not
    n = int(input("Enter a positive integer: "))

    is_prime = True

    if n < 2:
        is_prime = False
    else:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                is_prime = False
                break

    if is_prime:
        print(n, "is a prime number.")
    else:
        print(n, "is not a prime number.")


def problem_31():
    # Take a positive integer from the user. Displaying an error message and prompting
    # for input again and again if the user enters invalid input (negative or zero)
    while True:
        n = int(input("Enter a positive integer: "))

        if n > 0:
            break
        else:
            print("Invalid input! Please enter a positive integer.")

    # Rest of the code using the valid positive integer 'n'
    print("Valid input:", n)


def problem_32():
    # Display negative of a number
    # Prompt the user to enter a number
    num = int(input("Enter a number: "))

    # Compute the negative of the number
    negative_num = -1 * num

    # Display the negative value
    print("Negative of", num, "is", negative_num)


def problem_33():
    #
    # Prompt the user to enter a number
    num = int(input("Enter a number: "))

    # Check if the number is negative
    if num < 0:
        num = -1 * num

    # Display the absolute value
    print("Absolute value:", num)


def problem_34():
    # Input 2 number and find if both are even, both are odd, or 1 even 1 odd.
    # Prompt the user to enter the first number
    num1 = int(input("Enter the first number: "))

    # Prompt the user to enter the second number
    num2 = int(input("Enter the second number: "))

    # Check the remainders
    remainder1 = num1 % 2
    remainder2 = num2 % 2

    # Determine the relationship between the numbers
    if remainder1 == 0 and remainder2 == 0:
        print("Both numbers are even")
    elif remainder1 == 1 and remainder2 == 1:
        print("Both numbers are odd")
    else:
        print("One number is even and one number is odd")


def problem_35():
    # input 3 numbers and find how many are odd.
    # Prompt the user to enter the first number
    num1 = int(input("Enter the first number: "))

    # Prompt the user to enter the second number
    num2 = int(input("Enter the second number: "))

    # Prompt the user to enter the third number
    num3 = int(input("Enter the third number: "))

    # Initialize count
    count = 0

    # Check if num1 is odd
    if num1 % 2 != 0:
        count += 1

    # Check if num2 is odd
    if num2 % 2 != 0:
        count += 1

    # Check if num3 is odd
    if num3 % 2 != 0:
        count += 1

    # Output the count
    print("Number of odd numbers:", count)


# def problem_36()
    # nput 3 numbers and print the 2 largest numbers/

    # Prompt the user to enter the first number
    num1 = int(input("Enter the first number: "))

    # Prompt the user to enter the second number
    num2 = int(input("Enter the second number: "))

    # Prompt the user to enter the third number
    num3 = int(input("Enter the third number: "))

    # Find the largest number
    if num1 >= num2 and num1 >= num3:
        largest = num1
    elif num2 >= num1 and num2 >= num3:
        largest = num2
    else:
        largest = num3

    # Print the largest number
    print("Largest number:", largest)

    # Find the second largest number
    if num1 >= num2 and num1 <= num3:
        second_largest = num1
    elif num2 >= num1 and num2 <= num3:
        second_largest = num2
    else:
        second_largest = num3

    # Print the second largest number
    print("Second largest number:", second_largest)


def problem_37():
    # Input a number and find if it is 2-digit positive integer or not
    # Prompt the user to enter a number
    num = int(input("Enter a number: "))

    # Check if the number is a two-digit positive integer
    if num >= 10 and num < 100:
        print("The number is a two-digit positive integer.")
    else:
        print("The number is not a two-digit positive integer.")


def problem_38():
    # Input a 2-digit number and find the absolute difference between its digits
    # Prompt the user to enter a 2-digit number
    num = int(input("Enter a 2-digit number: "))

    # Extract the tens digit and units digit
    tens = num // 10
    units = num % 10

    # Calculate the absolute difference between the digits
    abs_diff = abs(tens - units)

    # Display the absolute difference
    print("The absolute difference between the digits is:", abs_diff)


def problem_39():
    # Input an integer (up to 4 digits) and store its reverse in another variable. Then
    # display both integers.
    # Prompt the user to enter a 4-digit integer
    num = int(input("Enter a 4-digit integer: "))

    # Initialize the variable to store the reversed integer
    reverse = 0

    # Extract the digits and create the reversed integer
    thousands = num // 1000
    hundreds = (num // 100) % 10
    tens = (num // 10) % 10
    units = num % 10

    reverse += thousands
    reverse += hundreds * 10
    reverse += tens * 100
    reverse += units * 1000

    # Display the original and reversed integers
    print("Original integer:", num)
    print("Reversed integer:", reverse)


def problem_40():
    # Interchange two numbers
    # Input the values of the two numbers
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    # Interchange the values using a temporary variable
    temp = num1
    num1 = num2
    num2 = temp

    # Display the updated values
    print("After interchanging:")
    print("First number:", num1)
    print("Second number:", num2)


def problem_41():
    # Interchange two numbers without using an extra variable
    # Input the values of the two numbers
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    # Interchange the values without using an extra variable
    num1 = num1 + num2
    num2 = num1 - num2
    num1 = num1 - num2

    # Display the updated values
    print("After interchanging:")
    print("First number:", num1)
    print("Second number:", num2)


def problem_42():
    # Multiply a number with the sum of its digits.
    # Input the number
    num = int(input("Enter a number: "))

    # Initialize the variable for digit sum
    digitSum = 0

    # Calculate the sum of the digits
    for digit in str(num):
        digitSum += int(digit)

    # Multiply the number with the sum of its digits
    result = num * digitSum

    # Display the result
    print("Result:", result)


def problem_43():
    #
    # Input the first number
    num1 = int(input("Enter the first number: "))

    # Input the second number
    num2 = int(input("Enter the second number: "))

    # Check if num1 is divisible by num2
    if num1 % num2 == 0:
        print("YES")
    else:
        print("NO")


def problem_44():
    # Input 2 numbers and print YES if 1st is divisible by 2nd
    # Input the first number
    num1 = int(input("Enter the first number: "))

    # Input the second number
    num2 = int(input("Enter the second number: "))

    # Check if num1 is divisible by num2 or num2 is divisible by num1
    if num1 % num2 == 0 or num2 % num1 == 0:
        print("YES")
    else:
        print("NO")


def problem_45():
    # Input numbers till user inputs a zero and display their sum
    # Initialize the sum variable
    sum = 0

    # Start the loop
    while True:
        # Prompt the user to enter a number
        num = int(input("Enter a number (enter 0 to stop): "))

        # Check if the entered number is 0
        if num == 0:
            break

        # Add the number to the sum
        sum += num

    # Print the sum
    print("The sum of the entered numbers is:", sum)


def problem_46():
    # Input numbers till user inputs a zero and at the end display last non-zero number
    # Initialize the last_non_zero variable
    last_non_zero = 0

    # Start the loop
    while True:
        # Prompt the user to enter a number
        num = int(input("Enter a number (enter 0 to stop): "))

        # Check if the entered number is 0
        if num == 0:
            break

        # Update the last_non_zero variable
        last_non_zero = num

    # Print the last non-zero number
    print("The last non-zero number entered is:", last_non_zero)


def problem_47():

    # Initialize the last_non_zero variable
    last_non_zero = 0

    # Start the loop
    while True:
        # Prompt the user to enter a number
        num = int(input("Enter a number (enter 0 to stop): "))

        # Check if the entered number is 0
        if num == 0:
            break

        # Update the last_non_zero variable
        last_non_zero = num

    # Print the last non-zero number
    print("The last non-zero number entered is:", last_non_zero)


def problem_48():
    # Input numbers till user inputs a zero and display the largest number
    # Initialize the largest variable
    largest = float('-inf')

    # Start the loop
    while True:
        # Prompt the user to enter a number
        num = int(input("Enter a number (enter 0 to stop): "))

        # Check if the entered number is 0
        if num == 0:
            break

        # Check if the entered number is larger than the current largest
        if num > largest:
            largest = num

    # Print the largest number
    print("The largest number entered is:", largest)


def problem_49():
    #  Input numbers till user inputs a zero, and display the smallest number
    # Initialize the smallest variable
    smallest = float('inf')

    # Start the loop
    while True:
        # Prompt the user to enter a number
        num = int(input("Enter a number (enter 0 to stop): "))

        # Check if the entered number is 0
        if num == 0:
            break

        # Check if the entered number is smaller than the current smallest
        if num < smallest:
            smallest = num

    # Print the smallest number
    print("The smallest number entered is:", smallest)


def problem_50():
    # Input 10 numbers, and display the smallest number
    # Initialize the smallest variable
    smallest = float('inf')

    # Start the loop for 10 iterations
    for _ in range(10):
        # Prompt the user to enter a number
        num = int(input("Enter a number: "))

        # Check if the entered number is smaller than the current smallest
        if num < smallest:
            smallest = num

    # Print the smallest number
    print("The smallest number entered is:", smallest)


def problem_51():
    #Input 10 numbers, and display count of even and odd numbers, separately, at the end
    # Initialize the count variables
    count_even = 0
    count_odd = 0

    # Start the loop for 10 iterations
    for _ in range(10):
        # Prompt the user to enter a number
        num = int(input("Enter a number: "))

        # Check if the number is even or odd
        if num % 2 == 0:
            count_even += 1
        else:
            count_odd += 1

    # Print the counts of even and odd numbers
    print("Count of even numbers:", count_even)
    print("Count of odd numbers:", count_odd)


def problem_52():
    # Input SLimit and Elimit from the user, and display even numbers between range,
    # with both limit, included.
    # Input start limit and end limit from the user
    SLimit = int(input("Enter the start limit: "))
    ELimit = int(input("Enter the end limit: "))

    # If the start limit is odd, increment it by 1 to make it even
    if SLimit % 2 != 0:
        SLimit += 1

    # Display even numbers between SLimit and ELimit (inclusive)
    print("Even numbers between", SLimit, "and", ELimit, "are:")
    for num in range(SLimit, ELimit + 1, 2):
        print(num)


def problem_53():
    # Input SLimit and ELimit from the user and display only those numbers between
    # range which are divisible by 2 or 3 or 5, with both limits included
    # Input start limit and end limit from the user
    SLimit = int(input("Enter the start limit: "))
    ELimit = int(input("Enter the end limit: "))

    # Display numbers divisible by 2, 3, or 5 between SLimit and ELimit (inclusive)
    print("Numbers divisible by 2, 3, or 5 between", SLimit, "and", ELimit, "are:")
    for num in range(SLimit, ELimit + 1):
        if num % 2 == 0 or num % 3 == 0 or num % 5 == 0:
            print(num)


def problem_54():
    # input 2 numbers and find their GCD
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    # Get input from the user
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    # Compute the GCD
    result = gcd(num1, num2)

    # Print the GCD
    print("The GCD of", num1, "and", num2, "is", result)


def problem_55():
    # Input 3 numbers and find their GCD
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    # Get input from the user
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    num3 = int(input("Enter the third number: "))

    # Compute the GCD of num1 and num2
    gcd1 = gcd(num1, num2)

    # Compute the GCD of gcd1 and num3
    result = gcd(gcd1, num3)

    # Print the GCD
    print("The GCD of", num1, ",", num2, "and", num3, "is", result)


def problem_56():
    # input 2 numbers and display their LCM.
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def lcm(a, b):
        return (a * b) // gcd(a, b)

    # Get input from the user
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    # Compute the LCM
    result = lcm(num1, num2)

    # Print the LCM
    print("The LCM of", num1, "and", num2, "is", result)


def problem_57():
    # Input a number and display that how many digits it has.
    # Get input from the user
    number = int(input("Enter a number: "))

    # Convert the number to a string and calculate the length
    num_str = str(number)
    num_digits = len(num_str)

    # Display the number of digits
    print("The number", number, "has", num_digits, "digits.")


def problem_58():
    #
    # Get input from the user
    number = int(input("Enter a number: "))

    # Convert the number to a string and calculate the length
    num_str = str(number)
    num_digits = len(num_str)

    # Display the number of digits
    print("The number", number, "has", num_digits, "digits.")


def problem_59():
    #
    # Get input from the user
    base_9_number = ""
    digit = input("Enter the most significant base-9 digit (0 to 8) or any other character to stop: ")

    # Continue getting digits until a non-base-9 digit is entered
    while digit.isdigit() and int(digit) < 9:
        base_9_number = digit + base_9_number
        digit = input("Enter the next base-9 digit or any other character to stop: ")

    # Convert the base-9 number to decimal
    decimal_number = 0
    power = len(base_9_number) - 1
    for i in range(len(base_9_number)):
        decimal_number += int(base_9_number[i]) * (9 ** power)
        power -= 1

    # Display the decimal number
    print("The decimal equivalent of", base_9_number, "is", decimal_number)


def problem_60():
    # Get input from the user
    decimal_number = int(input("Enter a decimal number: "))

    # Convert the decimal number to base-9
    base_9_number = ""
    while decimal_number > 0:
        remainder = decimal_number % 9
        base_9_number = str(remainder) + "\n" + base_9_number
        decimal_number = decimal_number // 9

    # Display the base-9 number
    print("The base-9 equivalent is:")
    print(base_9_number.strip())  # Remove leading/trailing whitespace and newline


def problem_61():
    # Get input from the user
    A = int(input("Enter the first number (A): "))
    B = int(input("Enter the second number (B): "))
    C = int(input("Enter the third number (C): "))

    # Sort the numbers in ascending order
    if A > B:
        A, B = B, A
    if B > C:
        B, C = C, B
    if A > B:
        A, B = B, A

    # Print the numbers in ascending order
    print("Numbers in ascending order:", A, B, C)


def problem_62():
    # Get input from the user
    number = int(input("Enter a decimal number: "))

    # Convert the number to base-9
    base_9 = 0
    power = 1

    while number > 0:
        digit = number % 9
        base_9 += digit * power
        power *= 10
        number //= 9

    # Display the base-9 equivalent
    print("Base-9 equivalent:", base_9)


def problem_63():
    # To check temperature
    if temperature >= 100 or pressure >= 200:
        print("Warning")
    else:
        print("OK")


def problem_64():
    #
    # To print reminder
    a = int(input("Enter the value of a: "))
    b = int(input("Enter the value of b: "))

    while a >= b:
        a -= b

    remainder = a

    print("The remainder of a/b is:", remainder)


def problem_65():
    # Input two positive integers and a and b from the user. Determine the integer of a/b
    # Division of 2 num
    a = int(input("Enter the value of a: "))
    b = int(input("Enter the value of b: "))

    quotient = 0

    while a >= b:
        a -= b
        quotient += 1

    print("The integer division of a/b is:", quotient)


def problem_66():
    # Input a decimal integer and display its hexadecimal equivalent digit-by-digit. The
    # hexadecimal output should be in order from least significant to most significant
    # Enter a decimal integer
    decimal = int(input("Enter a decimal integer: "))

    hexadecimal = ""

    while decimal > 0:
        remainder = decimal % 16
        hexadecimal = str(remainder) + hexadecimal
        decimal = decimal // 16

    print("The hexadecimal equivalent is:", hexadecimal)


def problem_67():
    # Conversion of microseconds to weeks, days, hours, minutes, seconds, and
      # remaining microseconds.
    total_microseconds = int(input("Enter the total number of microseconds: "))

    # Calculate weeks
    weeks = total_microseconds // (7 * 24 * 60 * 60 * 1000000)
    remaining_microseconds = total_microseconds % (7 * 24 * 60 * 60 * 1000000)

    # Calculate days
    days = remaining_microseconds // (24 * 60 * 60 * 1000000)
    remaining_microseconds = remaining_microseconds % (24 * 60 * 60 * 1000000)

    # Calculate hours
    hours = remaining_microseconds // (60 * 60 * 1000000)
    remaining_microseconds = remaining_microseconds % (60 * 60 * 1000000)

    # Calculate minutes
    minutes = remaining_microseconds // (60 * 1000000)
    remaining_microseconds = remaining_microseconds % (60 * 1000000)

    # Calculate seconds
    seconds = remaining_microseconds // 1000000
    remaining_microseconds = remaining_microseconds % 1000000

    print("Weeks:", weeks)
    print("Days:", days)
    print("Hours:", hours)
    print("Minutes:", minutes)
    print("Seconds:", seconds)
    print("Remaining Microseconds:", remaining_microseconds)


def problem_68():
    # Input two positive integers a and b from the user. Determine the remainder of a/b.
    # Assume that the division and modulus operators are not available
    # Input an integer
    num = int(input("Enter an integer (up to 4 digits): "))

    # Store the reverse of the integer
    reverse_num = 0

    # Calculate the reverse by extracting the digits and building the reversed number
    while num > 0:
        digit = num % 10
        reverse_num = (reverse_num * 10) + digit
        num //= 10

    # Display the original and reversed integers
    print("Original integer:", num)
    print("Reversed integer:", reverse_num)


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
    # problem_21()
    # problem_22()
    # problem_23()
    # problem_24()
    # problem_25()
    # problem_26()
    #  problem_27()
    #  problem_28()
    #  problem_29()
    #  problem_30()
    #  problem_31()
    #  problem_32()
    # problem_33()
    # problem_34()
    # problem_35()
    # problem_36()
    # problem_37()
    # problem_38()
    # problem_39()
    # problem_40()
    # problem_41()
    # problem_42()
    # problem_43()
    # problem_44()
    # problem_45()
    # problem_46()
    # problem_47()
    # problem_48()
    # problem_49()
    # problem_50()
    # problem_51()
    # problem_52()
    # problem_53()
    # problem_54()
    #  problem_55()
    #  problem_56()
    #  problem_57()
    #  problem_58()
    #  problem_59()
    #  problem_60()
    #  problem_61()
    #  problem_62()
    #  problem_63()
    #  problem_64()
    #  problem_65()
    #  problem_66()
    #  problem_67()
    problem_68()
