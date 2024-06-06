def median(nums):
    Sortnums = sorted(nums)
    L = len(Sortnums)

    if L%2 == 0:
        M_left = Sortnums[L//2 -1]
        M_Right = Sortnums[L//2 +1]
        return (M_left+M_Right)/2
    else:
        return Sortnums[L//2]
    
numbers = []
n = int(input("Enter number of numbers : "))

for i in range(n):
    numbers.append(int(input("Enter number : ")))

print("Median:", median(numbers))