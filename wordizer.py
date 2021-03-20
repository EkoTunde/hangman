from english_words import english_words_lower_alpha_set

# print(english_words_set)

with open('words.py','a') as f:
    f.write("words = [")
    for word in english_words_lower_alpha_set:
        if len(word) > 4:
            f.write(f"\"{word}\",")
    f.write("]")