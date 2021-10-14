num_years = 5
interest_rate = 5.0
amount = 80

for year in range(1, num_years + 1):
    interest = (interest_rate/100) * amount
    amount = amount + interest
    print('After ' + str(year) + ' years, ', end='')
    print('amount = ' + str(amount))
