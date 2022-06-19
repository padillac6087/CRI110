# This program will take the cost and figure the tip, tax, and total
#06/18/2022
#CTI-110 P2HW1 - Meal Tip Tax Calculator
#Christina V Padilla
#Ask user to enter cost of food
cost = float(input('Enter Food Cost: '))
print()
#Ask user to enter percentage for tip and tax
tip = float(input('Enter Tip Percentage: '))
tax = int(input('Enter Tax Percentage: '))
#take users cost and multiply it by tip, then divide by 100 to get correct amount
tip_ttl = float((cost*tip)/100)
#Take users cost and multiply it by tax, then divide it by 100 to get correct amount
tax_ttl = float((cost*tax)/100)
#To get the total add cost, tip total, and tax total
ttl = float(cost+tax_ttl+tip_ttl)
print()
#Display calculated tip total
print('Calculated Tip:\t$', format(tip_ttl, ',.2f'))
#Display calculated tax total
print('Calculated Tax:\t$', format(tax_ttl, ',.2f'))
print()
#Display calculate total
print('Total cost including tip and tax:  $', format(ttl, ',.2f'))

