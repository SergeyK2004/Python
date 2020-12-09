sentence = input("Введите предложение:")
word_list = sentence.split()
for nom, element in enumerate(word_list):
    print(nom + 1, element[:10])
