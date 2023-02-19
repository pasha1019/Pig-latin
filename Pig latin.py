print('Введите слово на английском языке')
word = input()
new_word = ''
spisok = "a,e,i,u,o"
if word[0].lower() in spisok:
    new_word = word + 'way'
else:
    for i in range(len(word)):
        if word[i] not in spisok:
            new_word = word[i+1:] + word[0:i+1]
        else:
            break
    new_word += 'ay'
print(new_word)
