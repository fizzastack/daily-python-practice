
text = input("Enter a string: ")

reverse = text[::-1]

if text.lower() == reverse.lower():
    print("Palindrome string")
else:
    print("Not a palindrome string")
