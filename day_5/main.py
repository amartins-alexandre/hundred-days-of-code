from bellman_ford import BellmanFord
from dijkstra import Dijsktra


# Write a program that implement a function to calculate the median of a list of numbers.
def median():
    numbers = [5, 2, 9, 21, 12, 3]
    numbers.sort()
    print(f"Sorted List: {numbers}")

    n = len(numbers)
    med = numbers[n // 2] if n % 2 != 0 else (numbers[n // 2 - 1] + numbers[n // 2]) / 2
    return med


# Write a program tha implement a algorithms to quick sort a list of numbers.
def quick_sort(array: list, low: int, high: int):
    if low < high:
        pi = partition(array, low, high)  # var pi = pivot index

        # put all smaller elements to the left of the pivot
        quick_sort(array, low, pi - 1)

        # put all higher elements to the right of the pivot
        quick_sort(array, pi + 1, high)


def partition(array: list, low: int, high: int) -> int:
    pivot = array[high]
    pi = low
    for n in range(low, high):
        if array[n] <= pivot:
            (array[pi], array[n]) = (array[n], array[pi])
            pi = pi + 1
    
    (array[pi], array[high]) = (array[high], array[pi])

    return pi
    

# Write a program that implements a algorithms to merge sort a number list
def merge_sort(array: list) -> list:
    if len(array) < 2:
        return array
    
    med = len(array) // 2
    left = merge_sort(array[:med])
    right = merge_sort(array[med:])

    return merge(left, right)


def merge(left: list, right: list):
    result = []
    r = 0
    l = 0
    
    # Ordenation
    while l < len(left) and r < len(right):
        if left[l] > right[r]:
            result.append(right[r])
            r = r + 1
        else:
            result.append(left[l])
            l = l + 1
    
    for n in range(l, len(left)):
        result.append(left[n])

    for n in range(r, len(right)):
        result.append(right[n])

    return result


if __name__ == "__main__":
    print("Day 5: Algorithms and Data Structures")
    print("Choose an option:")
    print("1 - Median")
    print("2 - Quick Sort")
    print("3 - Merge Sort")
    print("4 - Bellman-Ford Algorithm")
    print("5 - Dijkstra Algorithm")
    option = int(input("Option: "))

    match option:
        case 1:
            med = median()
            print(f"Median: {med}")
        case 2:
            numbers = [10, 90, 50, 80, 40, 30, 70]
            print(f"Unsorted: {numbers}")
            
            quick_sort(numbers, 0, len(numbers) - 1)
            print(f"Sorted: {numbers}")
        case 3:
            numbers = [10, 90, 50, 80, 40, 30, 70]
            print(f"Unsorted: {numbers}")
            
            sorted = merge_sort(numbers)
            print(f"Sorted: {sorted}")
        case 4:
            graph = BellmanFord(6)
            graph.add_edge(0, 1, 5)
            graph.add_edge(0, 2, 4)
            graph.add_edge(1, 3, 3)
            graph.add_edge(2, 1, 6)
            graph.add_edge(3, 2, 2)
            graph.add_edge(3, 4, 6)
            graph.add_edge(4, 0, 3)
            graph.add_edge(4, 5, 7)
            graph.add_edge(5, 0, 1)
            graph.add_edge(5, 2, 4)

            graph.start(0)
        case 5:
            graph = Dijsktra(7)
            graph.add_edge(0, 1, 2)
            graph.add_edge(0, 2, 6)
            graph.add_edge(1, 3, 8)
            graph.add_edge(2, 3, 8)
            graph.add_edge(3, 5, 15)
            graph.add_edge(3, 4, 10)
            graph.add_edge(3, 6, 5)
            graph.add_edge(4, 6, 2)
            graph.add_edge(5, 6, 3)

            graph.start(0)
        case _:
            print('Invalid option')