# Write a program that prints "Hello World!" on the screen.
def write_hello_world():
    print("Hello World!")

# Write a program that asks the user for their name and then prints "Hello, [name]!" on the screen.
def write_hello_name():
    name = input("What's your name? ")
    print(f"Hi, {name}!")

# Write a program that calculates the sum of two integers entered by the user and prints the result.
def sum_two_integers():
    number1 = int(input("Write the first number: "))
    number2 = int(input("Write the second number: "))
    print(f"The sum of two numbers are {number1 + number2}")

# Write a program that verify if a number entered by the user is even or odd.
def verify_even_or_odd():
    number = int(input("Write a number: "))
    if number % 2 == 0:
        print("The number is even.")
    else:
        print("the number is odd.")

# Write a program that asks the user for a string and then prints it inverted.
def invert_string():
    string = input("Write a string: ")
    print(string[::-1])

# Write a program that determines if a string entered by the user is a palindrome.
def verify_palindrome():
    string = input("Write a string: ")
    if string == string[::-1]:
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")


if __name__ == "__main__":
    # Choice a option to run
    print("1 - Write Hello World!")
    print("2 - Write Hello Name!")
    print("3 - Sum two integers!")
    print("4 - Verify if a number is even or odd!")
    print("5 - Invert a string!")
    print("6 - Verify if a string is a palindrome!")
    option = int(input("Choose a option: "))

    match option:
        case 1:
            write_hello_world()
        case 2:
            write_hello_name()
        case 3:
            sum_two_integers()
        case 4:
            verify_even_or_odd()
        case 5:
            invert_string()
        case 6:
            verify_palindrome()
        case _:
            print("Invalid option!")
