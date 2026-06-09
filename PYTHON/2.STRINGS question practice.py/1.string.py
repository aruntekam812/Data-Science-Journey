#Ek string me vowels count karo.
# s = input("Enter string: ")

# count = sum(1 for ch in s.lower() if ch in "aeiou")

# print(count)
s = input().lower()

if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

