# This program will take the cost and figure the tip, tax, and total
#06/18/2022
#CTI-110
#P3HW2 - MealTipTax
#Christina V Padilla

#Ask user to enter cost of the meal and tip
def main():
    cost = float(input('Please enter cost of meal: '))
    tip = float(input('Enter tip amount of 15, 18, or 20: '))
    print()
#Calculations for totals needed
    tip_ttl = float((cost*tip)/100)
    tax_ttl = float(cost*0.06)
    ttl = float(cost+tip_ttl+tax_ttl)
#Depending on tip entered it will show the user their amounts
    if tip == 15:
        print('Meal price:\t$', format(cost, ',.2f'))
        print('Tax:\t$', format(tax_ttl, ',.2f'))
        print('Tip:\t$', format(tip_ttl, ',.2f'))
        print('Total:  $', format(ttl, ',.2f'))

    elif tip == 18:
        print('Meal price:\t$', format(cost, ',.2f'))
        print('Tax:\t$', format(tax_ttl, ',.2f'))
        print('Tip:\t$', format(tip_ttl, ',.2f'))
        print('Total:  $', format(ttl, ',.2f'))

    elif tip == 20:
        print('Meal price:\t$', format(cost, ',.2f'))
        print('Tax:\t$', format(tax_ttl, ',.2f'))
        print('Tip:\t$', format(tip_ttl, ',.2f'))
        print('Total:  $', format(ttl, ',.2f'))
#If the user enters an invalid amount they will receive an error message
    else:
        print('Error: Must enter tip of either 15, 18, or 20')

main()
