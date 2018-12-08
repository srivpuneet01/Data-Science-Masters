def filter_long_words(collection,maxLength):
    iterableCollection = iter(collection)
    return filter(lambda word : len(word) > maxLength, iterableCollection)

print(list(filter_long_words(["asdadasdfasfderew","asdfxcze","qwqww"], 6)))