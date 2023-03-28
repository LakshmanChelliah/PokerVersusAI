from poker import *

import time

NUMBER_OF_AI = 1
STARTING_BALANCE = 100
#[user, bot1, bot2]

currentPerson = 0
roundNum = 0

previousBet = 0
betList = []
#  balanceList = []

#Increments the  index of the next player in the lists
def incrementStartingPerson(x)-> int:
    if x == NUMBER_OF_AI:
        return 0 
    else:
        return x + 1
    
#initalizes the lists to hold all the players current bets
def initBetList()-> list:
    temp = [0]
    for i in range(NUMBER_OF_AI):
        temp.append(0)

    return temp

#initializes the lists to hold all the players current balances
def initBalances()-> list:
    temp = [STARTING_BALANCE]
    for i in range(NUMBER_OF_AI):
        temp.append(STARTING_BALANCE)

    return temp

#function to allow the user to bet
def bet(index:int, bet:int,betList,balanceLIst) -> bool:
    print("bet: " + str(bet))
    if validateBet(index,bet,balanceLIst):
        betList[index] += bet
        previousBet = bet
        
        balanceLIst[index] -= bet
        return True
    else:
        return False
def match(index):
#code that finds largest number in betList
    temp = 0
    for bet in betList:
        if temp < bet:
            temp = bet 
    
    return (temp - betList[index])

    
def matchPreviousBet(index, balanceLIst):
    
    #betList[index] += match(index)
   
    bet(index,match(index),betList,balanceLIst)
    
    print("before")
    #print(balanceLIst[index])
    balanceLIst[index] -=  match(index)
    print("after")
   # print(balanceLIst[index])
    
def getPreviousWager(index):
    if index == 0:
        if betList[-1] == -1:
            return getPreviousWager[betList,-1]
        return betList[-1]
    else:
        if betList[index-1] == -1:
            return getPreviousWager[betList,index-1]
        return betList[index-1]


def validateBet(index, bet, balanceList)->bool:
    if balanceList[index] < bet:
        return False
    else:
        return True
    
def stand(index)->bool:
    if previousBet == 0 or getPreviousWager(index) == betList(index):
        return True
    else:
        False


def fold(index)->bool:
    balanceList[index] -= betList[index]
    betList[index] = -1




if __name__ == "__main__":

    deck = makeDeck()

    gameDeck = deck.copy()
    shuffleDeck(gameDeck)

    hands = dealCards(gameDeck,NUMBER_OF_AI)

    betList = initBetList()
    balanceList = initBalances()
   
#----------------------------------------------------
    def standOrFold(index):
        print("Fold or Stand")
        if stand(index) == False:
            print("Fold")
            fold(index)
        print("Stand")


    def actionBasedOnHand(chance, index, odds,balanceList):
        if chance == 10:
            if odds >=0:
                matchPreviousBet(index,balanceList)
                bet(index, random.randint(0,20),betList,balanceList)
        elif chance == 9:
            if odds >=1:
                matchPreviousBet(index,balanceList)
                bet(index, random.randint(0,20),betList,balanceList)
            else:
                standOrFold(index)
        elif chance == 8:
            if odds >=1:
                matchPreviousBet(index,balanceList)
                bet(index, random.randint(0,20),betList,balanceList)
            else:
                standOrFold(index)
        elif chance == 7:
            if odds >=1:
                matchPreviousBet(index,balanceList)
                bet(index, random.randint(0,20),betList,balanceList)
            else:
                standOrFold(index)
        elif chance == 6:
            if odds >=1:
                matchPreviousBet(index,balanceList)
                bet(index, random.randint(0,20),betList,balanceList)
            else:
                standOrFold(index)
        elif chance == 5:
            if odds >=1:
                matchPreviousBet(index,balanceList)
                bet(index, random.randint(0,20),betList,balanceList)
            else:
                standOrFold(index)
        elif chance == 4:
            if odds >=2:
                matchPreviousBet(index,balanceList)
                bet(index, random.randint(0,20),betList,balanceList)
            else:
                standOrFold(index)
        elif chance == 3:
            if odds >=3:
                matchPreviousBet(index,balanceList)
                bet(index, random.randint(0,10),betList,balanceList)
            else:
                standOrFold(index)
        elif chance == 2:
            if odds >=4:
                matchPreviousBet(index,balanceList)
                bet(index, random.randint(0,10),betList,balanceList)
            else:
                standOrFold(index)
        elif chance == 1:
            if odds >=5:
                matchPreviousBet(index,balanceList)
                bet(index, random.randint(0,5),betList,balanceList)
            else:
                standOrFold(index)
        elif chance == 0:
            if odds >=6:
                matchPreviousBet(index,balanceList)
                print(betList)
                bet(index, random.randint(0,5),betList,balanceList)
            else:
                standOrFold(index)
                
                



    roundNum = 0
    while True:
        
        
        print("bets:")
        print(betList)
        print("balance:")
        print(balanceList)

        if roundNum == 0:
            print(hands[0])
            next = input("'S'tand\n'R'aise\n'F'old\n")

            if next.upper() == 'S':
                print("Standing")
                stand(0)

            elif next.upper() == 'R':
                print("Raising")
                wager = input("How much to increase bet? ")
                print(balanceList)
                bet(0, int(wager),betList,balanceList)
                print(balanceList)
                

            elif next.upper() == 'F':
                print("Folding")
                fold(0)

            for i in range(1,NUMBER_OF_AI+1):
                
                odds = random.randint(5,10)
                print(hands[i])
                chance = checkChances(hands[i],[])
                time.sleep(2)
                print("chance: " + str(chance))
                print("odds: " + str(odds))
                actionBasedOnHand(chance, i, odds, balanceList)
                print("bets:")
                print(betList)
                print("balance:")
                print(balanceList)

                if getPreviousWager(i) > betList[i]:
                    
                    print("AI HAS FOLDED")
                
                elif getPreviousWager(i) < betList[i]:

                    print(hands[0])
                    next = input("'M'atch\n'R'aise\n'F'old\n")

                    if next.upper() == 'M':
                        print("Matching")
                        matchPreviousBet(0,balanceList)

                    elif next.upper() == 'R':
                        print("Raising")
                        wager = input("How much to increase bet? ")
                        print(balanceList)
                        bet(0, int(wager),betList,balanceList)
                        print(balanceList)
                        

                    elif next.upper() == 'F':
                        print("Folding")
                        fold(0)

                print("bets:")
                print(betList)
                print("balance:")
                print(balanceList)
                
                  


                



        break
        
                        



        






            

       

        

 
