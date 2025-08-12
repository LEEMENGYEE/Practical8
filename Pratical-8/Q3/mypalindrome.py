def is_palindrome(input_string):
    input_string = normalize_case(remove_noise(input_string))
    return input_string == input_string[::-1]

def normalize_case(input_string):
    return input_string.lower()
    
    
def remove_noise(input_string):
    return "".join([letter if letter.isalpha() else "" for letter in input_string])