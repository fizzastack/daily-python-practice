
numbers = list(map(int, input("Enter numbers: ").split()))

frequency = {}

for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

for num, count in frequency.items():
    print(num, "appears", count, "times")
