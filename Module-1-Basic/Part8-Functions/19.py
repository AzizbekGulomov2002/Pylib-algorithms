


def count_vowels(word):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in word:
        if char in vowels:
            count+=1
    return count

word = input("So'z kiriting = ")
result = count_vowels(word)
print(f"So'zdagi unlilar soni: {result}")