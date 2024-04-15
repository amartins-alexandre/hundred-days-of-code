"""
Write a program that prints a sequence numbers of Fibonacci intil of N-th term, 
where N is a number inserted by the user.
"""
def fibonnaci():
    n = int(input("Enter a number: "))
    f = [0, 1]
    for i in range(2, n):
        f.append(f[i-1] + f[i-2])
    
    print(f)

# Write a program that verify if a number inserted by the user in a prime number.
def is_prime():
    n = int(input("Enter a number: "))
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                print(f"Number {n} isn't prime")
                break
        else:
            print(f'Number {n} is prime')
    else:
        print(f"Number {n} isn't prime")
    

# Write a program that reads a list of numbers by the user and prints only the even numbers.
def even_numbers():
    numbers = input("Enter a list of numbers: ")
    numbers = numbers.replace(',', '').split()
    numbers = list(map(int, numbers))
    even_numbers = []
    for number in numbers:
        if number % 2 == 0 and number not in even_numbers:
            even_numbers.append(number)
    print(even_numbers)


# Write a program that implement a funtion for calculate a power of a number.
def power_number():
    base = int(input("Enter a number: "))
    exp = int(input("Enter a power of this number: "))

    result = base
    if exp > 1:
        result = base ** exp
    
    print(f'The result of this calculate is: {result}')

# Write program that order a list of number inserted by the user in crescent order.
def crescent_order():
    numbers = input("Enter a list of numbers: ")
    numbers = numbers.replace(',', '').split()
    numbers.sort()
    print(list(map(int, numbers)))


# Write a program that calculate the factorial of the number inserted by the user.
def factorial():
    number = int(input(f'Enter a number: '))
    if number < 0:
        print("Factorial does not exist for negative numbers")
    elif number == 0:
        print("The factorial of 0 is 1")
    else:
        result = 1
        for n in range(1, number + 1):
            result = result * n
        print(f'The factorial of {number} is {result}')


# Write a program that dertemine if a list of number inserted by the user is ordered in crescent order.
def is_crescent_order():
    numbers = input("Enter a list of numbers: ")
    numbers = list(map(int, numbers.replace(',', '').split()))
    crescent_order = numbers
    crescent_order.sort()
    print(f'The list is ordered in crescent order' 
          if numbers == crescent_order else 'The list is not ordered in crescent order')


if __name__ == "__main__":
    # Choice a option to run
    print("1 - Write sequence numbers of Fibonacci!")
    print("2 - Verify it's a prime number!")
    print("3 - Read a list number and prints only even numbers!")
    print("4 - Calculate a power of a number!")
    print("5 - Order a list of number in crescent order!")
    print("6 - Write factorial of one number!")
    print("7 - Verify if a list of number is oredered in crescent order!")
    option = int(input("Choose a option: "))

    match option:
        case 1:
            fibonnaci()
        case 2:
            is_prime()
        case 3:
            even_numbers()
        case 4:
            power_number()
        case 5:
            crescent_order()
        case 6:
            factorial()
        case 7:
            is_crescent_order()
        case _:
            print("Invalid option!")