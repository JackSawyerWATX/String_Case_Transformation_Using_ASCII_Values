

1. transform_char(c) Function:

    Lowercase Check: If c is between 'a' and 'z', convert it to uppercase by subtracting 32 from its ASCII value.
    Uppercase Check: If c is between 'A' and 'Z', convert it to lowercase by adding 32 to its ASCII value.
    Non-Letter Characters: Return them unchanged.

2. solution(input_string) Function:

    Iterates over each character in input_string.
    Applies transform_char to each character to get the transformed character.
    Collects the transformed characters in a list and joins them into a single string to return.