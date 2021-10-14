num_years = 20
interest_rate1 = 8
interest_rate2 = 3
amount1 = 1000
amount2 = 1000
for year in range(1, num_years + 1):
    interest1 = (interest_rate1/100) * amount1
    amount1 = amount1 + interest1

for year in range(1, num_years + 1):
    interest2 = (interest_rate2/100) * amount2
    amount2 = amount2 + interest2

print('The 8% fund exceeds the 3% by ' + str(amount1 - amount2))
