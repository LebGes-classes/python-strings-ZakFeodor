import re

text = input('Введите текст ')

alf_down = 'abcdefghijklmnopqrstuvwxyz'
alf_up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
splited_text = ''
lower_text = ''
check_text = ''

for symbol in text:
    if symbol in alf_up:
        for i in range(len(alf_up)):
            if alf_up[i] == symbol:
                lower_text += alf_down[i]
    else:
        lower_text += symbol

all_words = re.findall(r"\b[\w']+\b", lower_text)
len_all_words = len(all_words)
checked_words = ''
count_top = 0

for k in range(len_all_words, 0, -1):
    for i in range(len_all_words):
        check_word = all_words[i]
        count = 0

        for j in range(len_all_words):
            current_word = all_words[j]

            if check_word == current_word:
                count += 1
        if count == k and check_word not in checked_words and count_top < 5:
            count_top += 1
            checked_words += check_word
            print(check_word)
