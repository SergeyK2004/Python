sentence = input("Введите предложение:")
word_list = sentence.split()
for i in range(len(word_list)):
    print(i + 1, word_list[i][:10])
