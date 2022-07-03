#Creating a score lits
#CTI-110
#P4HW1 - Score List
#Christina V Padilla
#07/03/2022

def main():
#Ask user for score number count    
    score_num = int(input('How many scores do you want to enter? '))

    print()

    list=[]
#Get score from user
    for i in range(1, score_num +1):

        score = float(input('Enter score #{}: '.format(i)))

        if score >= 0 and score <= 100:
            list.append(score)

        else:

            while score < 0 or score > 100:
                print('Invalid Score Entered!!!')
                print('score Should be between 0 and 100')
                score=float(input('Enter Score #{} again: ' .format(i)))
                list.append(score)

    print()
    print()
    print('--------------Results-------------')
#Print results
    lowestscore=min(list)
    print('Lowest Score : ', lowestscore)
    
    list.remove(lowestscore)
    print('Modified List: ', list)

    avgoflist=sum(list)/len(list)
    print('Score Average: ',format(avgoflist,',.2f'))

    if avgoflist >= 90:
        print('Grade        :  A')
    
    elif avgoflist >= 80:
        print('Grade        :  B')
    
    elif avgoflist >= 70:
        print('Grade        :  C')
    
    elif avgoflist >= 60:
        print('Grade        :  D')
    
    else:
        print('Grade        :  E')

    print('-----------------------------------')

main()
