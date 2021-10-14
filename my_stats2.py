n = 100
total = 0

for k in range(1, n+1, 2):
    total = total + k

avg = total / n
print('Average=' + str(avg))
