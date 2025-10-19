text = input('Введите текст ')

new_text = ''
word = ''

for k in range(len(text)-1, -1, -1):
    if text[k] == ' ':
        new_text += word + ' '
        word = ''
    else:
        word = text[k] + word

    if k == 0:
        new_text += word
        word = ''

text = new_text
new_text = ''
word = ''

for i in range(len(text)):
    if text[i] != ' ':
        word += text[i]
    else:
        for j in range(len(word)):
            new_text += word[-j - 1]
        new_text += ' '
        word = ''

    if i == len(text) - 1:
        for j in range(len(word)):
            new_text += word[-j - 1]
        word = ''

print(new_text)