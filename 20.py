def get_first_and_last_chars(input_string):
    if len(input_string) < 2:
        return "String length is less than 2, cannot proceed."
    
    result_string = input_string[:2] + input_string[-2:]
    return result_string

user_input = input("Enter a string: ")
result = get_first_and_last_chars(user_input)
print(result)
