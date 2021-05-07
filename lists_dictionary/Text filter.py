    string = input().split(', ')
    text = input()
    for word in string:
        while word in text:
            text = text.replace(word, ("*" * len(word)))
    print(text)