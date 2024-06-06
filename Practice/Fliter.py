print("\nWith Lambda function")
def filterPos(numbers):
    pos_numbers = list(filter(lambda x: x>0,numbers))

    return pos_numbers

numbers = [-1, 2, -3, 4, -5, 6]
print("List of numbers : ",numbers)
print("Positive numbers:", filterPos(numbers))


print("\nWithout Lambda functions")

def is_positive(x):
    return x > 0

def extract_positive_numbers(numbers):
    positive_numbers = list(filter(is_positive, numbers))
    return positive_numbers

# Example usage:
numbers = [-1, 2, -3, 4, -5, 6]
positive_numbers = extract_positive_numbers(numbers)
print("Positive numbers:", positive_numbers)