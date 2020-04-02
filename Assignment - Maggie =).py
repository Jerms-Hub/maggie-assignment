
print('Question I : ')
product = int(input('Enter the number of products sold : '))

if (product < 50):
    print('Bonus : $100 for the first 50 products')
    Bonus = 0
    print('Weekly bonus on sale = '+ '$'+ str(Bonus))

if (product == 50):
    print('Bonus : $100 for the first 50 products')
    Bonus = 100
    print('Weekly bonus on sale = '+ '$'+ str(Bonus))

if (product > 50):
    print('Bonus : $5 per product for over 50 products')
    Bonus = 100 + product * 5
    print('Weekly bonus on sale = '+ '$'+ str(Bonus))

print('Question II : ')
Monday = int(input('Monday sales : '))
Tuesday = int(input('Tuesday sales : '))
Wednesday = int(input('Wednesday sales : '))
Thursday = int(input('Thursday sales : '))
Friday = int(input('Friday sales : '))
Saturday = int(input('Saturday sales : '))
Sunday = int(input('Sunday sales : '))

sales = Monday + Tuesday + Wednesday + Thursday + Friday + Saturday + Sunday
print('Total weekly sales : '+ str(sales))

average = int(sales / 7)
print('Average weekly sales : ' + str(average))
