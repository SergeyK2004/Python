def int_func(word):
    new_word = word[0].upper() + word[1:]
    return new_word

user_str = input("Введите строку:")
user_words_list = user_str.split()
new_word_list = map(int_func, user_words_list)

result = " ".join(new_word_list)
print(result)