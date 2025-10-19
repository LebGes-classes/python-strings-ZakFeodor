import re

received_text = input('Введите текст ')

word = ''
text = ''
new_text = ''
alf_down = 2*'abcdefghijklmnopqrstuvwxyz'
alf_up = 2*'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
K = 0
dot_count = 0

for symbol in received_text:
    if symbol == '.':
        dot_count += 1

for word in re.findall(r"\b[\w']+\b", received_text):
    if len(word) > K:
        K = len(word)
    text += word + ' '

if K > 20 or dot_count > 1:
    print('Введен текст, не подходящий по условию')
else:
    for symbol in text:
        if symbol in alf_down:
            for i in range(len(alf_down)//2):
                if alf_down[i] == symbol:
                    new_text += alf_down[i+K]
        elif symbol in alf_up:
            for i in range(len(alf_up)//2):
                if alf_up[i] == symbol:
                    new_text += alf_up[i+K]
        else:
            new_text += symbol

    print(new_text, K)
    