n = 1000
total = 0
term = 1/2
for k in range(n):
    total = total + term
    term = term * (1/2)

print(total)