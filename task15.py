'''Count vowels and consonants in string.
Normal: "hello" → (2,3)
Edge: "" → (0,0)
Only vowels: "aeiou" → (5,0)
Large: Long text
'''
def count_vowels_consonants(s):
    """Count the number of vowels and consonants in a given string."""
    vowels = 'aeiouAEIOU'
    vowel_count = sum(1 for char in s if char in vowels)
    consonant_count = sum(1 for char in s if char.isalpha() and char not in vowels)
    return vowel_count, consonant_count
# Example usage
print(count_vowels_consonants("hello"))
print(count_vowels_consonants(""))
print(count_vowels_consonants("aeiou"))
    