def count_characters(input_string):

    char_frequency = {}

    for char in input_string:

        if char in char_frequency:

            char_frequency[char] += 1
        else:

            char_frequency[char] = 1


    for char, count in char_frequency.items():
        print(f"'{char}': {count}")


input_string = "programming is fun"
count_characters(input_string)
