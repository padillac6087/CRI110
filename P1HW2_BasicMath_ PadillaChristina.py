#Find the expense for each month and the whole year
#06/11/2022
#CTI-110 P1HW2 - Basic Math
#Christina V Padilla
#This will take basic whole amts and calculate NC sales tax to find mth and yr amt

bill = input('Enter name of expense: ')
amt = int(input('Enter monthly charge: '))
tax = (amt*0.0475)
ttl = (amt+tax)
print()
print('Bill:', bill, '--------- Before Tax: $', format(amt, ',.2f'))
print('Monthly Tax:     $', format(tax, ',.2f'))
print('Monthly Charge:  $', format(amt+tax,',.2f'))
print('Annual Charge:   $', format(12*ttl,',.2f'))

