#Creating a program to show expenses
#CTI-110
#P4HW2 - Expenses
#Christina V Padilla
#07/03/2022

def main():

#Ask user for starting amout
    s_amt = float(input('Enter starting amount in account $'))

    count = 1

    more = 'y' or 'Y'
#Need to keep count and total    
    amt = 0
    sum = 0

    while more=='y' or more=='Y':
      amt = float(input('\nEnter expense '+str(count)+': '))
      sum += amt
      more = input('Do you want to enter another expense? (y/n) ')
      if more=='y' or more=='Y':
        count += 1
    print()
    ttl = s_amt - sum
#Print information
    print('Amount in account before expenses subtracted $',format(s_amt,'.2f'))
    print('Number of expenses entered: ',count)
    print('Amount in account after expenses subtracted is $',format(ttl,',.2f'))

main()
