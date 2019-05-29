file = open('命运.txt', 'rt')
word_list = {}
for word in file.read():
    if word not in ['\n', ' ']:
        word_list[word] = int(word_list.get(word, '0')) + 1
word_list = list(word_list.items())
word_list.sort(key=lambda x: x[1], reverse=True)
for i in range(10):
    print("{}:{}".format(word_list[i][0], word_list[i][1]))
