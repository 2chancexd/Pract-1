def process_string(input_string):
    vowels = "aeiouAEIOU"
    consonant_letters = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    
    vowels_in_string = [char for char in input_string if char in vowels]
    consonants_in_string = [char for char in input_string if char in consonant_letters]
    
    sorted_vowels = sorted(vowels_in_string, reverse=True)
    sorted_consonants = sorted(consonants_in_string, reverse=True)
    
    more_than_three_vowels = len(sorted_vowels) > 3
    
    return (''.join(sorted_vowels), more_than_three_vowels, ''.join(sorted_consonants))

input_string = "abcdefg"
result = process_string(input_string)
print(result)  