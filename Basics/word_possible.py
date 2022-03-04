mix_word = input("What are your mixed characters: \n")
phrase = input("What word would like to like: \n")


def make_word(character, word):
    if len(character) <= 0:
        return False
    if len(word) == 0:
        return True
    ch_array = list(character)
    for i in word:
        if i in ch_array:
            ch_array.pop(ch_array.index(i))
        else:
            return False
    return True
print(make_word(mix_word, phrase))
