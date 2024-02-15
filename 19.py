def reverse_string_if_multiple_of_4(input_string):
    if len(input_string) % 4 == 0:
        return input_string[::-1]
    else:
        return input_string


result = reverse_string_if_multiple_of_4("abcdefgh")
print(result)
