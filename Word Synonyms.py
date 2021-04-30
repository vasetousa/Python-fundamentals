n = int(input()) # count of words
synonyms = {}
test = {}
for el in range(n):
    word = input()
    synonym = input()
    if word not in synonyms:
        synonyms[word] = []
        synonyms[word].append(synonym)
    else:
        synonyms[word].append(synonym)
for word in synonyms:
    print(f"{word} - {', '.join(synonyms[word])}")
print()
for key, values in synonyms.items():    # same as above print, but using ".items()"
    print(f"{key} - {', '.join(values)}")
