from random import choice
def random_words():
    words = {"Ars": 20, "Raha": 19, "Almaz": 19}
    word = choice(["Ars", "Raha", "Almaz"])
    hint = words[word]
    return word,hint
print(random_words())

