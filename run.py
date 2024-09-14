def solution(input_string):
    # TODO: implement the function
    def transform_char(c):
        # Check if the character is a lowercase letter
        if 'a' <= c <= 'z':
            return chr(ord(c) - 32)  # Convert to uppercase
        # Check if the character is an uppercase letter
        elif 'A' <= c <= 'Z':
            return chr(ord(c) + 32)  # Convert to lowercase
        # Return the character unchanged if it's not a letter
        else:
            return c
    
    result = []
    for char in input_string:
        result.append(transform_char(char))
    
    return ''.join(result)

print(solution("HelLo WoRld 123"))
