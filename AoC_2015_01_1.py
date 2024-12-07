f_in = open('input_2015_01.txt', 'r', encoding='utf-8')
text = f_in.readlines()
f_in.close()
print(text[0].count('(') - text[0].count(')'))
i = 0
cur = 0
while cur >= 0:
    if text[0][i] == '(':
        cur += 1
    else:
        cur -= 1
    i += 1
print(i)