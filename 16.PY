def add_ing_or_ly(input_str):
    if len(input_str) >= 3:
        if input_str.endswith('ing'):
            return input_str + 'ly'
        else:
            return input_str + 'ing'
    else:
        return input_str


input_string = "read"
result = add_ing_or_ly(input_string)
print(result)
