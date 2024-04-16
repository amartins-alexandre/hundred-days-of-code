from utils import map_to_int_list


# Write a program that calculates the averange of the number in a list inserted by the user.
def averange_number():
    numbers = input("Enter a list of numbers: ")
    numbers= map_to_int_list(numbers)
    avg = sum(numbers) / len(numbers)

    print(f'The averange of numbers in the list: {round(avg, 2)}')


"""
Write a programa that implements a binary search in a ordered list of number inserted by the user.

Here's a step-by-step description of using binary search in a ordered list of number:
1. Let min_index = 0 and max_index = n-1, where n is the number of elements in the list.
2. Guess the average of min_index and max_index, rounded down so that it is an integer.
3. If you guessed the number, stop. You found it!
4. If the guess was too high, set min_index to be one larger than the guess.
5. If the guess was too low, set max_index to be one smaller than the guess.
6. Go back to step two.
"""
def binary_search():
    numbers = input("Enter a list of numbers: ")
    numbers = map_to_int_list(numbers)
    numbers.sort()

    min_index = 0
    max_index = len(numbers) - 1
    guess = (min_index + max_index) // 2
    tries = 0

    print(f'Think of a number between {str(min(numbers))} and {str(max(numbers))}!')
    while True:
        print(f'Guess: {numbers[guess]}')
        tries += 1
        
        answer = input("Is the number higher, lower or correct? (h, l or c): ")
        match(answer):
            case 'h':
                min_index = guess + 1
            case 'l':
                max_index = guess - 1
            case 'c':
                print(f'The number is {numbers[guess]} and the tries was {tries}')
                break
            case _:
                print('Invalid option!')

        guess = (min_index + max_index) // 2



# Write a program that determines if a string inserted by the user is a pangram.
def is_pangram():
    sentence = input("Enter a sentence: ")
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    pangram = True
    for char in alphabet:
        if char not in sentence:
            pangram = False
    
    print('This sentence is a pangram' if pangram else 'This sentence is not a pangram')
    


# Write a program that get everthings prime numbers until a limit inserted by the user.
def prime_numbers():
    limit = int(input("Enter a limit: "))

    # List comprehension to get all prime numbers
    prime_numbers = [n for n in range(2, limit + 1) if all(n % i != 0 for i in range(2, n))]
    print(f'Prime numbers: {prime_numbers}')


# Write a program that implements a function for calculate a numbers of combination of 'n' objects taken from 'r' in 'r'.
# Formula: C(n, r) = n! / (r! * (n - r)!)
def factorial(number: int) -> int:
    return 0 if number > 0 else (number + factorial(number - 1))
    

def calculate_combinations():
    n = int(input("Enter a number of objects: "))
    r = int(input("Enter a number of objects taken from 'n': "))
    result = factorial(n) / (factorial(r) * factorial(n - r))
    print(f'The numbers of combination of {n} objects taken from {r} in {r} is {result}')

"""
Write a program that implements a function for calculate a square root of the number using the Newton's method.

Formula: root = 0.5 * (X + (N / X))
Approach: The following steps can be followed to compute the answer: 

1. Assign X to the N itself.
2. Now, start a loop and keep calculating the root which will surely move towards the correct square root of N.
3. Check for the difference between the assumed X and calculated root, if not yet inside tolerance then update root and continue.
4. If the calculated root comes inside the tolerance allowed then break out of the loop.
5. Print the root.
"""
def sqrt_newton(tolerance: float = 0.00001):
    n = int(input("Enter a number: "))
    x = n

    while abs(x - n / x) > tolerance:
        x = 0.5 * (x + (n / x))
    
    print(f'The square root of {n} is {round(x, 2)}')


# Write a program that implements a linear search in the inserted list by the user.
def linear_search():
    list_data = input('Enter a list: ').replace(',', '').split()
    target = input('Enter a target: ')
    index = -1

    for k, v in enumerate(list_data):
        if v == target:
            index = k

    if index == -1:
        print(f'The target {target} was not found in the list')
    else:    
        print(f'The target {target} was found in the list at index {index}')



if __name__ == "__main__":
    # Choice a option to run
    print("1 - Calculate the averange of the number!")
    print("2 - Binary search!")
    print("3 - Is a pangram?")
    print("4 - Get everthings prime numbers!")
    print("5 - Calculate a numbers of combination!")
    print("6 - Square root of the number using the Newton's method!")
    print("7 - Linear search!")
    option = int(input("Choose a option: "))

    match option:
        case 1:
            averange_number()
        case 2:
            binary_search()
        case 3:
            is_pangram()
        case 4:
            prime_numbers()
        case 5:
            calculate_combinations()
        case 6:
            sqrt_newton()
        case 7:
            linear_search()
        case _:
            print("Invalid option!")
