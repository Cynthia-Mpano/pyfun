def kajipotefu_convert(text):
    # Create the transformation dictionary
    conversion_dict = {
        'k': 'a', 'a': 'k',
        'j': 'i', 'i': 'j',
        'p': 'o', 'o': 'p',
        't': 'e', 'e': 't',
        'f': 'u', 'u': 'f',
        'K': 'A', 'A': 'K',
        'J': 'I', 'I': 'J',
        'P': 'O', 'O': 'P',
        'T': 'E', 'E': 'T',
        'F': 'U', 'U': 'F'
    }

    # Convert the input string
   
    result = ""
    
    for char in text:
        result += conversion_dict.get(char, char)  # If char not in dict, keep it unchanged
    
    return result

# Test the function
user_input = input("Enter a string: ")
converted_str = kajipotefu_convert(user_input)
print("KAJIPOTEFU converted string:", converted_str)
