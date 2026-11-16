
numbers = list(map(int, input("Enter numbers: ").split()))

largest = None
second_largest = None

for num in numbers:
    if largest is None or num > largest:
        second_largest = largest
        largest = num

    elif num != largest and (
        second_largest is None or num > second_largest
    ):
        second_largest = num

if second_largest is None:
    print("Second largest number does not exist")
else:
    print("Second largest:", second_largest)
