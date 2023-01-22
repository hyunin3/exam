def get_secret_number(words):
    result = 0
    for word in words:
        result = result + ord(word)
    return result    

print(get_secret_number('happy'))
