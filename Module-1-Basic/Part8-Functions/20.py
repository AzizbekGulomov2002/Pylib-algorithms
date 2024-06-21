

def count_vowels(word):
    vowels = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    count = 0
    for char in word:
        if char in vowels:
            count += 1
    return count

# Test
word = input("So'z kiriting: ")
result = count_vowels(word)
print(f"So'zdagi undoshlar soni: {result}")