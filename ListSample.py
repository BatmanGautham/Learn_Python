def traversal(lst):
    print("List elements:")
    for num in lst:
        print(num, end=" ")
    print()

def sort_list(lst):
    lst.sort()
    print("Sorted list:", lst)

def min_max(lst):
    print("Minimum value:", min(lst))
    print("Maximum value:", max(lst))

def append_squares(lst):
    squares = [num**2 for num in lst]
    lst.extend(squares)
    print("List after appending squares:", lst)


def main():
    numbers = []
    n = int(input("Enter the number of elements: "))
    print("Enter the elements:")
    for _ in range(n):
        element = int(input("Enter element: "))
        numbers.append(element)

    while True:
        print("\nMenu:")
        print("1. Traverse list")
        print("2. Sort list")
        print("3. Print Min and Max values")
        print("4. Append squares of elements")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            traversal(numbers)
        elif choice == 2:
            sort_list(numbers)
        elif choice == 3:
            min_max(numbers)
        elif choice == 4:
            append_squares(numbers)
        elif choice == 5:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

main()
