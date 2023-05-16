from datetime import datetime


def find_quotiant(a, b):
    print(float(a / b))


def sum_of_four():
    first = int(input('Enter first mnumber: '))
    second = int(input('Enter second mnumber: '))
    third = int(input('Enter third mnumber: '))
    four = int(input("Enter fourth number: "))
    sum_of_num = first + second + third + four
    print(sum_of_num)
    return sum_of_num


def average_of_students():
    inputs = []
    for i in range(5):
        value = input(f"Enter {i} Student value: ")
        inputs.append(int(value))
    sum_of_students = sum(inputs)
    average = sum_of_students / 5
    print(sum_of_students, average)
    return sum_of_students, average


def percentage_of_students(a, b, c, d):
    total = 400
    sum_of_students = a + b + c + d
    percentage = sum_of_students / total * 100
    print(f"{percentage}%")
    return percentage


def check_number(num):
    if num > 80:
        print('good')
    else:
        print("Try again")


def check_divisible():
    num = int(input('Give a number: '))
    diviser = int(input("Check if it's divisble on: "))
    if num % diviser == 0:
        print("its divideable")
    else:
        print("not divideable")


def sum_of_odd():
    total = 0
    for i in range(10):
        number = int(input('Enter any Number'))
        if number % 2 == 0:
            continue
        else:
            total += number
    print(total)


def sum_of_even():
    range_of_num = int(input("How many numbers you wanna give: "))
    total = 0
    for i in range(range_of_num):
        number = int(input('Enter any Number: '))
        if number % 2 == 0:
            total += number
    print(total)


def fibonnaci_series(n):
    series = [0, 1]
    if n <= 2:
        print(series[:n])
    for iteration in range(n - 2):
        fibonnaci_num = series[-1] + series[-2]
        series.append(fibonnaci_num)
    print(series)


def farenhiet_to_celcius(n):
    celcius = (n - 32) * (5 / 9)
    print(int(celcius))


def calculate_pay():
    hours_worked = int(input("How many hours have u worked: "))
    rate_per_hour = int(input("What is your rate per hour: "))
    print(f"Your pay will be {rate_per_hour * hours_worked}")


def calculate_overtime_pay():
    hours_worked = int(input("How many hours have u worked: "))
    rate_per_hour = int(input("What is your rate per hour: "))
    if hours_worked <= 40:
        regular_pay = hours_worked * rate_per_hour
        print(f"Your Regular Pay is {regular_pay}$")
        return regular_pay
    regular_pay = 40 * rate_per_hour
    extra_hours = hours_worked - 40
    bonus_wage = rate_per_hour + rate_per_hour / 2
    bonus_pay = extra_hours * bonus_wage
    print(f"Your Regular Pay is {regular_pay}$ and bonus pay is {bonus_pay}$")


def find_two_largest():
    first_num = int(input("Enter first number: "))
    second_num = int(input("Enter first number:"))
    if first_num > second_num:
        print(f"{first_num} is the largest")
    elif first_num < second_num:
        print(f"{second_num} is the largest")
    else:
        print('Both number are equal')


def find_largest_nested_if():
    first_num = int(input("Enter first number: "))
    second_num = int(input("Enter first number:"))
    third_num = int(input('Enter the third number'))
    if first_num > second_num:
        if first_num > third_num:
            print(f"{first_num} is the largest")
            return
    if second_num > first_num:
        if second_num > third_num:
            print(f"{second_num} is the largest")
            return
    if third_num > second_num:
        if third_num > first_num:
            print(f"{third_num} is the largest")
            return
    print('No largest found numbers might be equal')


def find_largest_compound() -> object:
    first_num = int(input("Enter first number: "))
    second_num = int(input("Enter first number:"))
    third_num = int(input('Enter the third number'))
    if first_num > second_num and first_num > second_num:
        print(f"{first_num} is the largest")
    elif second_num > first_num and second_num > third_num:
        print(f"{second_num} is the largest")
    elif third_num > first_num and third_num > second_num:
        print(f"{second_num} is the largest")
    else:
        print('No largest number found numbers might be equal')


def find_largest_first_large():
    first_num = int(input("Enter first number: "))
    second_num = int(input("Enter first number:"))
    third_num = int(input('Enter the third number:'))
    fourth_num = int(input('Enter the third number:'))
    largest = first_num
    if second_num > largest:
        largest = second_num
    if third_num > largest:
        largest = third_num
    if fourth_num > largest:
        largest = fourth_num
    print(f"{largest} is the largest number")


def calculate_grade():
    marks = int(input("Enter the marks obtained:"))
    if 90 <= marks <= 100:
        print('A')
    elif 80 <= marks < 90:
        print('B')
    elif 70 <= marks < 80:
        print('C')
    elif 60 <= marks < 70:
        print('D')
    elif marks > 100:
        print("Marks can't be more than 100")
    else:
        print('F')


def check_even_odd():
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        print('Number is even')
    else:
        print('number is odd')


def diff_in_time(time1, time2):
    time1 = datetime(time1, '%H:%M').time()
    time2 = datetime(time2, '%H:%M').time()
    print(time)


def sum_of_ten():
    total = 0
    for i in range(10):
        num = int(input('Enter a number: '))
        total += num
    print(total)


def sum_of_n():
    n = int(input('How many numbers you want to add: '))
    total = 0
    for i in range(n):
        num = int(input('Enter a number: '))
        total += num
    print(total)


def average_of_n():
    n = int(input('How many numbers you want to add: '))
    total = 0
    for i in range(n):
        num = int(input('Enter a number: '))
        total += num
    avg = total / n


def find_range(n):
    for i in range(1, n + 1):
        print(i)


def find_fictorial(n):
    fictorial = 1
    for i in range(2, n + 1):
        fictorial *= i
    print(fictorial)


def calculate_n(a, n):
    total = 1
    for i in range(n):
        total *= a
    print(total)


def largest_three_using_loop():
    numbers = []
    for i in range(3):
        num = int(input("Enter a Number:"))
        numbers.append(num)
    largest = numbers[1]
    for n in numbers:
        if n > largest:
            largest = n
    print(f'Largest Number is {largest}')


def largest_n_number():
    n = int(input("How many numbers you want to add: "))
    numbers = []
    for i in range(n):
        num = int(input("Enter a number:"))
        numbers.append(num)
    largest = numbers[0]
    for numbers in numbers:
        if numbers > largest:
            largest = numbers
    print(largest)


if __name__:
    # find_quotiant(12, 4)
    # sum_of_four()
    # average_of_students()
    # percentage_of_students(90, 90, 90, 90)
    # check_number(90)
    # check_divisible()
    # sum_of_odd()
    # sum_of_even()
    # fibonnaci_series(20)
    # farenhiet_to_celcius(50)
    # calculate_pay()
    # calculate_overtime_pay()
    # find_two_largest()
    # find_largest_nested_if()
    # find_largest_compound()
    # find_largest_first_large() # suitable approach for 4 numbers
    # calculate_grade()
    # check_even_odd()
    diff_in_time("22:40", "12:00")
    # sum_of_ten()
    # sum_of_n()
    # average_of_n()
    # find_range(10)
    # find_fictorial(10)
    # calculate_n(2, 5)
    # largest_three_using_loop()
    # largest_n_number()
