import wordtool

n = 10
total = 0

for k in range(1, n+1):
    word = wordtool.get_random_verb()
    total = total + len(word)

avg = total / n
print('Average word length = ' + str(avg))