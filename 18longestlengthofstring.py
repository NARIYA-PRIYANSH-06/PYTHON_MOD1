def find_longest_word(words):
    if not words:
        return 0
    
    longest_length=len(words[0])

    for word in words[1:]:
        current_length=len(word)
        if longest_length<=current_length:
            longest_length=current_length
    return longest_length

words_list=["priyansh","dheyey","mayank","yash","nevil","maulik"]
result=find_longest_word(words_list)
print("longest word length of list is: ",result)
