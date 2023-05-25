from datetime import datetime
# import numpy as np
import sys
import math


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
    percentage = (sum_of_students / total) * 100
    print(f"{percentage}%")
    return percentage


def check_number(num):
    if num > 80:
        print('good')
    else:
        print("Try again")


def check_divisible():
    # fixme what of diviser = 0 ?
    num = int(input('Give a number: '))
    diviser = int(input("Check if it's divisble on: "))
    if num == 0 or diviser == 0:
        print("0 can't be a valid divisor or divident")
    elif num % diviser == 0:
        print("its divideable")
    else:
        print("not divideable")


def sum_of_odd():
    # fixme if user enter even numbers ?
    total = 0
    odd_counter = 0
    while odd_counter < 10:
        number = int(input('Enter a Number'))
        if number % 2 == 0:
            continue
        else:
            total += number
            odd_counter += 1
    print(total)


def sum_of_even():
    # fixme if user enter odd numbers ?
    range_of_num = int(input("How many even numbers you wanna give: "))
    total = 0
    even_counter = 0
    while even_counter < range_of_num:
        number = int(input('Enter a Number'))
        if number % 2 == 0:
            total += number
            even_counter += 1
        else:
            continue
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
    elif second_num > first_num:
        if second_num > third_num:
            print(f"{second_num} is the largest")
    elif third_num > second_num:
        if third_num > first_num:
            print(f"{third_num} is the largest")
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
    # fixme if user enter 0?
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        print('Number is even')
    else:
        print('number is odd')


def diff_in_time():
    time1 = input('Enter Time in hh:mm format: ')
    time2 = input('Enter Time in hh:mm format: ')
    time1 = datetime.strptime(time1, '%H:%M')
    time2 = datetime.strptime(time2, '%H:%M')
    print(time2 - time1)


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
    for i in range(0, n):
        print(i)


def find_fictorial(n):
    fictorial = 1
    # enuirate try this
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


def find_small_and_large():
    n = int(input("How many numbers you want to add: "))
    numbers = []
    for i in range(n):
        num = int(input("Enter a number:"))
        numbers.append(num)

    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number

    smallest = numbers[0]
    for number in numbers:
        if number < smallest:
            smallest = number
    print(largest, smallest)


def num_of_negative_or_positive(n):
    num_of_positive = 0
    num_of_negative = 0
    numbers = []
    for i in range(n):
        num = int(input("Enter a Number: "))
        numbers.append(num)
    for num in numbers:
        if num > 0:
            num_of_positive += 1
        if num < 0:
            num_of_negative += 1
    print(f"You gave {num_of_positive} positive and {num_of_negative} negative integers")


def find_divisor():
    n = int(input("Enter a number: "))
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    print(divisors)
    return divisors


def find_perfect_positive():
    n = int(input("Enter a number: "))
    divisors = []
    for i in range(1, n):
        if n % i == 0:
            divisors.append(i)

    if sum(divisors) == n:
        print("Perfect Positive Number")
    else:
        print('Not a perfect positive Number')


def find_prime():
    n = int(input("Enter a number: "))
    for i in range(2, n):
        if n % i == 0:
            print("Not a prime number")
            break
    print("Prime Number")


def take_positive_only():
    not_positive = True
    while not_positive:
        n = int(input("Enter a number:"))
        if n > 0:
            not_positive = False
            print("Its Positive")
        else:
            print('Not Positive', file=sys.stderr)


def sum_until_sentinal():
    sentinal_prov = False
    numbers = []
    while sentinal_prov == False:
        n = int(input("Enter a number:"))
        if n == -999:
            sentinal_prov = True
        else:
            numbers.append(n)
    print(sum(numbers))


def display_negative():
    n = int(input("Enter a Number to make it negative:"))
    negative = n - (n + n)
    print(negative)


def find_abs():
    n = int(input('Enter a number to make it absolute:'))
    if n >= 0:
        print(f"Absolute Value is {n}")
    else:
        absolute = n - (n + n)
        print(f"Absolute Value is {absolute}")


def find_two_even_odd():
    n1 = int(input('Enter first number: '))
    n2 = int(input("Enter second number: "))
    if n1 % 2 == 0 and n2 % 2 == 0:
        print("Both are even")
    elif n1 % 2 != 0 and n2 % 2 != 0:
        print('Both are odd')
    else:
        print("One is even and One is odd")


def find_odd_from3():
    numbers = []
    no_of_odd = 0
    for i in range(3):
        n = int(input("Enter a number: "))
        numbers.append(n)
    for number in numbers:
        if number % 2 != 0:
            no_of_odd += 1
    print(f'There are {no_of_odd} odd numbers')


def find_2_largest():
    numbers = []

    for i in range(3):
        n = int(input("Enter a number: "))
        numbers.append(n)
    smallest = numbers[0]
    for number in numbers:
        if number < smallest:
            smallest = number
    smallest_index = numbers.index(smallest)
    numbers.pop(smallest_index)
    print(f"Two largest numbers are {numbers}")


def find_2digit_int():
    n = int(input('Enter a number: '))
    if len(str(n)) == 2:
        print("It is a 2 digit number.")
    else:
        print("Not a valid two digit number")


def find_abs_diff_2digit():
    n = input("Enter a two digit number: ")
    abs_diff = abs(int(n[0]) - int(n[1]))
    print(abs_diff)


def reverse_integer():
    # todo without using list comprehension
    number = input('Enter a number: ')
    length = len(number) - 1
    reverse_int = ''
    while True:
        if length < 0:
            break
        reverse_int += number[length]
        length -= 1
    print(reverse_int)


def interchange_numbers():
    a = int(input("Enter First number:"))
    b = int(input("Enter Second number:"))
    c = a
    a = b
    b = c
    print(a, b)


def interchange_without_var():
    # fixme me without using python function
    a = int(input('Enter a first Number:'))
    b = int(input('Enter Second Number:'))
    b, a = a, b
    print(a, b)


def multiply_sum_digit():
    n = input('Enter a Multi-digit number:')
    digits = []
    for digit in n:
        digits.append(int(digit))
    digit_sum = sum(digits)
    print(int(n) * digit_sum)


def first_divisible_second():
    first_num = int(input('Enter First Number:'))
    second_num = int(input('Enter Second Number:'))
    if first_num % second_num == 0:
        print('YES')


def second_divisible_first():
    first_num = int(input('Enter First Number:'))
    second_num = int(input('Enter Second Number:'))
    if second_num % first_num == 0:
        print('YES')


def each_other_divisble():
    first_num = int(input('Enter First Number:'))
    second_num = int(input('Enter Second Number:'))
    if second_num % first_num == 0 or first_num % second_num == 0:
        print('YES')


def zero_sentinal():
    sentinal_prov = False
    numbers = []
    while sentinal_prov == False:
        n = int(input("Enter a number:"))
        if n == 0:
            sentinal_prov = True
        else:
            numbers.append(n)
    print(sum(numbers))


def sentinal_last_nonzero():
    sentinal_prov = False
    numbers = []
    while sentinal_prov == False:
        n = int(input("Enter a number:"))
        if n == 0:
            sentinal_prov = True
        else:
            numbers.append(n)
    print(numbers[-1])


def sentinal_largest():
    sentinal_prov = False
    numbers = []
    largest = 0
    while sentinal_prov == False:
        n = int(input("Enter a number:"))
        if n == 0:
            sentinal_prov = True
        else:
            numbers.append(n)
            if n > largest:
                largest = n
    print(f"Largest Value is: {largest}")


def sentinal_smallest():
    sentinal_prov = False
    numbers = []
    while sentinal_prov == False:
        n = int(input('Enter a number: '))
        if n == 0:
            break
        if len(numbers) == 0:
            numbers.append(n)
            smallest = n
            continue
        if n < smallest:
            smallest = n
    print(smallest)


def small_from_10():
    numbers = []
    for i in range(10):
        n = int(input('Enter Any Numbers:'))
        numbers.append(n)
    smallest = numbers[0]
    for number in numbers:
        if number < smallest:
            smallest == number
    print(smallest)


def even_odd_from_10():
    no_of_odd = 0
    no_of_even = 0
    for i in range(10):
        n = int(input('Enter a Number:'))
        if n % 2 == 0:
            no_of_even += 1
        else:
            no_of_odd += 1
    print(f"Number of Even numbers are: {no_of_even}")
    print(f"Number of Odd numbers are: {no_of_odd}")


def even_range_Limit():
    Slimit = int(input('Enter Slimit:')) + 1
    Wlimit = int(input('Enter Elimit:'))
    even_range = []
    for i in range(Slimit, Wlimit):
        if i % 2 == 0:
            even_range.append(i)
    print(even_range)


def divisble_range():
    Slimit = int(input('Enter Slimit:')) + 1
    Wlimit = int(input('Enter Elimit:'))
    divisble_range = []
    for i in range(Slimit, Wlimit):
        if i % 2 == 0 or i % 3 == 0 or i % 5 == 0:
            divisble_range.append(i)
    print(divisble_range)


def find_GCD():
    # fixme do it without using math/numpy
    num1 = find_divisor()
    num2 = find_divisor()
    common_divisors = np.intersect1d(num1, num2)
    GCD = np.max(common_divisors)
    print(f"GCD of two number is {GCD}")


def find_three_GCD():
    # fixme do it without using math/numpy
    num1 = find_divisor()
    num2 = find_divisor()
    num3 = find_divisor()
    common_divisors = np.intersect1d(num1, num2, num3)
    GCD = np.max(common_divisors)
    print(f"GCD of three numbers is: {GCD}")


def find_lcm():
    # fixme do it without using math/numpy
    num1 = int(input('Enter a Number :'))
    num2 = int(input('Enter a Number :'))
    print(math.lcm(num1, num2))


def find_digit():
    n = int(input('Enter a Number: '))
    print(len(str(n)))


def digits_to_num():
    sentinal_prov = False
    numbers = []
    while sentinal_prov == False:
        n = int(input("Enter a number:"))
        if n == 9:
            sentinal_prov = True
        else:
            numbers.append(n)
    decimal = int(''.join(map(str, numbers)))
    print(f"Decimal number is {decimal}")


def digits_to_num_reverse():
    sentinal_prov = False
    numbers = []
    while sentinal_prov == False:
        n = int(input("Enter a number:"))
        if n == 9:
            sentinal_prov = True
        else:
            numbers.append(n)
    print(numbers)
    numbers = numbers[::-1]
    print(numbers)
    decimal = int(''.join(map(str, numbers)))
    print(f"Decimal number is {decimal}")


def convert_base_9_obo():
    # fixme do it without using math/numpy
    n = int(input('Enter a Number:'))
    quotient = n
    converted = False
    remainders = []
    while converted == False:
        remainder = quotient % 9
        remainder = remainders.append(remainder)
        quotient = math.floor(quotient / 9)
        if quotient == 0:
            converted = True
    for number in remainders:
        print(number)


def convert_base_9_decimal():
    digits = []
    sentinal_given = False
    decimal = 0
    power = 0
    # Getting data one by one
    while sentinal_given == False:
        n = int(input('Enter a Number: '))
        if n == 9:
            sentinal_given = True
        else:
            digits.append(n)
    digits = reversed(digits)

<<<<<<< HEAD
    # Base 9 to decimal
=======
    # Base 9 to decimal 
>>>>>>> 42fc8810fa9bfc011763726cfd1ef012d12255db
    for digit in digits:
        decimal += digit * (9 ** power)
        power += 1
    print(f" Decimal value is : {decimal}")


def convertBase9ToBinary():
    digits = []
    sentinal_given = False
    decimal = 0
    power = 0
    # Getting data one by one
    while sentinal_given == False:
        n = int(input('Enter a Number: '))
        if n == 9:
            sentinal_given = True
        else:
            digits.append(n)
    digits = reversed(digits)

<<<<<<< HEAD
    # Base 9 to decimal
=======
    # Base 9 to decimal 
>>>>>>> 42fc8810fa9bfc011763726cfd1ef012d12255db
    for digit in digits:
        decimal += digit * (9 ** power)
        power += 1
    print(decimal)
    binary = ''
    quotient = decimal

    # decimal to binary
    while True:
        quotient, remainder = divmod(quotient, 2)
        binary += str(remainder)
        if quotient == 1:
            break
    print(f"Base 9 to Binary is : {binary}")


def convertToHexa():
    remainders = []
    quotient = int(input('Enter a Number: '))
    converted = False
    while converted == False:
        remainder = quotient % 16
        quotient = int(quotient / 16)
        remainders.append(remainder)
        if quotient == 0:
            converted = True
    remainders = reversed(remainders)
    for remainder in remainders:
        string_num = str(remainder)
        num = string_num.replace('10', 'A').replace('11', 'B').replace('12', 'C').replace('13', 'D').replace('14',
                                                                                                             'E').replace(
            '15', 'F')
        print(num)


def ascending_order():
    A = int(input('Enter a Number'))
    B = int(input('Enter a Number'))
    C = int(input('Enter a Number'))
    num = [A, B, C]
    num.sort()
    print(num)


def pressure_temp_warning():
    pressure = int(input('Enter Value of Pressure: '))
    temp = int(input('Enter Value of Pressure: '))
    if temp >= 100 or pressure >= 200:
        print('WARNING')


def division_mod_without_operator():
    divident = int(input("Enter the divident: "))
    divisor = int(input('Enter the divisor: '))
    quotient = 0
    while divident >= divisor:
        divident -= divisor
        quotient += 1

    print(f"a/b is = {quotient}")
    print(f'Remainder is = {divident}')


def mircorseconds_to_other_time():
    microseconds = int(input('Enter micorseconds'))
    weeks, microseconds = divmod(microseconds, 7 * 24 * 60 * 60 * 10 ** 6)
    days, microseconds = divmod(microseconds, 24 * 60 * 60 * 10 ** 6)
    hours, microseconds = divmod(microseconds, 60 * 60 * 10 ** 6)
    minutes, microseconds = divmod(microseconds, 60 * 10 ** 6)
    seconds, microseconds = divmod(microseconds, 10 ** 6)
    print(f"Weeks: {weeks}")
    print(f"Days: {days}")
    print(f"Hours: {hours}")
    print(f"minutes: {minutes}")
    print(f"Seconds: {seconds}")
    print(f"Microseconds: {microseconds}")


def count_vowels(words):
    for word in words:
        original = word
        word = word.lower()
        vowels = ['a', 'e', 'i', 'o', 'u']
        no_of_vowels = 0
        for vowel in vowels:
            while True:
                # if the vowel exist it will keep removing it
                if vowel in word:
                    no_of_vowels += 1
                    word = word.replace(vowel, '', 1)
                else:
                    break
        print(f"{original} has {no_of_vowels} vowels ")


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
    # find_largest_first_large() suitable approach for 4 numbers
    # calculate_grade()
    # check_even_odd()
    # diff_in_time()
    # sum_of_ten()
    # sum_of_n()
    # average_of_n()
    # find_range(10)
    # find_fictorial(10)
    # calculate_n(2, 5)
    # largest_three_using_loop()
    # largest_n_number()
    # find_small_and_large()
    # num_of_negative_or_positive(3)
    # find_divisor()
    # find_perfect_positive()
    # find_prime()
    # take_positive_only()
    # sum_until_sentinal()
    # display_negative()
    # find_abs()
    # find_two_even_odd()
    # find_odd_from3()
    # find_2_largest()
    # find_2digit_int()
    # find_abs_diff_2digit()
    reverse_integer()
    # interchange_numbers()
    # interchange_without_var()
    # mircorseconds_to_other_time()
    # multiply_sum_digit()
    # first_divisible_second()
    # second_divisible_first()
    # each_other_divisble()
    # zero_sentinal()
    # sentinal_last_nonzero()
    # sentinal_largest()
    # sentinal_smallest()
    # small_from_10()
    # even_odd_from_10()
    # even_range_Limit()
    # divisble_range()
    # find_GCD()
    # find_three_GCD()
    # find_lcm()
    # # find_digit()
    # digits_to_num()
    # digits_to_num_reverse()
    # convert_base_9_obo()
    # convert_base_9_decimal()
    # convertBase9ToBinary()
    # convertToHexa()
    # ascending_order()
    # pressure_temp_warning()
<<<<<<< HEAD
    # division_mod_without_operator()
=======
    # division_mod_without_operator() 
>>>>>>> 42fc8810fa9bfc011763726cfd1ef012d12255db
    # count_vowels(['Apple', 'Orange', 'aam']