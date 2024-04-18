from bfs import Root, bfs
from dfs import Graph


# Write a program that converts a decimal number inserted by the user into binary.
def decimal_to_binary():
    decimal = input("Enter a decimal number: ")
    decimal = bin(int(decimal))
    print(f"Binary: {decimal}")
    

# Write a program that implements a function to calculate the moving average of a list of numbers.
def moving_average():
    numbers = input("Enter a list of numbers separated by spaces: ")
    numbers = list(map(int, numbers.split()))
    window = int(input("Enter the window size: "))
    moving_average = []
    for i in range(len(numbers) - window + 1):
        moving_average.append(round(sum(numbers[i:i+window]) / window, 2))
    print(f"Moving average: {moving_average}")


# Write a program that implements a function to calculate the scalar product of two vectors.
def scalar_product():
    a = [x for x in range(2, 5)]
    b = [x for x in range(3, 6)]

    scalar_product = sum([a[i] * b[i] for i in range(len(a))])
    assert scalar_product == 38

    print(f"Scalar product: {scalar_product}")


if __name__ == "__main__":
    print("Day 4: Algorithms and Data Structures")
    print("Choose an option:")
    print("1 - Decimal to Binary")
    print("2 - Moving Average")
    print("3 - BFS")
    print("4 - DFS")
    print("5 - Scalar Product")
    option = int(input("Option: "))

    match option:
        case 1:
            decimal_to_binary()
        case 2:
            moving_average()
        case 3:
            root = Root(1)
            root.children = [Root(2), Root(3)]
            root.children[0].children = [Root(4), Root(5)]
            root.children[1].children = [Root(6), Root(7)]
            bfs(root)
        case 4:
            g = Graph()
            g.add_edge(0, 1)
            g.add_edge(0, 2)
            g.add_edge(0, 3)
            g.add_edge(1, 0)
            g.add_edge(2, 4)
            g.add_edge(2, 0)
            g.add_edge(2, 3)
            g.add_edge(3, 0)
            g.add_edge(3, 2)
            g.add_edge(4, 2)
            g.dfs(2)  # 2 4 0 1 3
        case 5:
            scalar_product()
        case _:
            print("Invalid option")
