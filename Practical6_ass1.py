text = input("Enter a string: ")

vowels_count = 0
consonants_count = 0
spaces_count = 0
lowercase_count = 0

vowels = "aeiouAEIOU"

for char in text:
    if char.islower():
        lowercase_count += 1
    
    if char == " ":
        spaces_count += 1
    elif char.isalpha():
        if char in vowels:
            vowels_count += 1
        else:
            consonants_count += 1

print(f"a) Number of Vowels: {vowels_count}")
print(f"b) Number of Consonants: {consonants_count}")
print(f"c) Number of Spaces: {spaces_count}")
print(f"d) Number of Lowercase Letters: {lowercase_count}")
