import re
from select import select


f = open(r'C:\Users\user\Desktop\Python\ERR.LOG')
t = f.read()
w = 'AMQ9638'

if w in t:
    c = t.count(w)
    print(c)

list_word = t.split("-----")

p = r'(\d+:\d+)'

for i in range(len(list_word)):
    if 'AMQ9638' not in list_word[i]:
        continue
    m = re.search(p, list_word[i])

    if m is None:
        continue

    print(m.group(1))
