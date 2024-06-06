numbers = [1,2,4,9,7,3]

print("Numbers are ",numbers)

count = 0

for number in numbers:
    if number%2 == 0:
        count += 1

print("Count of even numbers:",count)
print("Count of odd numbers:", len(numbers)-count)