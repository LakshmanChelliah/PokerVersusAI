import random 


NUMBER_OF_AI = 2
STARTING_BALANCE = 100
#user is player 0 
players = []
table = []

def makeDeck()->list:
    deck = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
    symbols = ["♠","♥","♦","♣"]
    
    finaldeck = [];

    for x in symbols:
        for y in deck:
            finaldeck.append([x,y])
   
    return finaldeck

def shuffleDeck(deck:list)->list:
    random.shuffle(deck)
    return deck

def dealCards(deck:list):

    shuffleDeck(deck)

    for i in range(NUMBER_OF_AI+1):
        cards = []
        for j in range(2):
            cards.append(deck.pop())
        players.append(cards)

def cardfortable(deck,x:int)->list:
    for i in range(x):
        table.append(deck.pop())
    return table

def checkChances(hand:list, table:list)->int:
    totalChance = 0
    #highcard is 1
    #pair is 2
    #two pair is 3
    #three of a kind is 4
    #straight is 5
    #flush is 6
    #full house is 7
    #four of a kind is 8
    #straight flush is 9
    #royal flush is 10

    
    cardsInPlay = [hand[0], hand[1]]
    
    for i in range(len(table)):
        cardsInPlay.append(table[i])

    #check for straight flush in cardsInPlay
    if checkStraight(cardsInPlay)[0] == True and checkFlush(cardsInPlay)[0] == True and checkFlush(cardsInPlay)[1] == checkStraight(cardsInPlay)[1]:

        #check for royal flush in cardsInPlay
        if checkFlush(cardsInPlay)[1][0] == '10':
            return 10
        return 9
        
    #check for four of a kind in cardsInPlay
    elif xOfaKind(cardsInPlay,4)[0] == True:
        return 8
        
    #Check for a full house in cardsInPlay
    elif checkFullHouse(cardsInPlay)[0] == True:
        return 7
    
    #check for a flush in cardsInPlay
    elif checkFlush(cardsInPlay)[0] == True:
        return 6
    
    #check for a straight in cardsInPlay
    elif checkStraight(cardsInPlay)[0] == True:

        return 5
    
    #check for three of a kind in cardsInPlay
    elif xOfaKind(cardsInPlay,3)[0] == True:
        return 4
    
    #check for two pair in cardsInPlay
    elif checkTwoPair(cardsInPlay)[0] == True:
        return 3
    
    #check for a pair in cardsInPlay
    elif xOfaKind(cardsInPlay,2)[0] == True:
        return 2
    
    elif checkHighCard(cardsInPlay)[1] == 'K' or checkHighCard(cardsInPlay)[1] == 'Q' or checkHighCard(cardsInPlay)[1] == 'J' or checkHighCard(cardsInPlay)[1] == 'A' or checkHighCard(cardsInPlay)[1] == '10':
        return 1
    
    else:
        return 0
   
    
    #check for a flush in cardsInPlay

def checkHighCard(AllCards:list)->list:    
    temp = sortValuesandNumerize(AllCards)
    actualValue = []
    for i in temp:
        if i == '1':
            temp.remove(i)
        else:
            actualValue.append(int(i)) 
            
    actualValue.sort()

    

    if actualValue[-1] == 11:
        return [True,'J']
    elif actualValue[-1] == 12:
        return [True,'Q']
    elif actualValue[-1] == 13:
        return [True,'K']
    elif actualValue[-1] == 14:
        return [True,'A']
    else:
        return [True,str(actualValue[-1])]

    

    return[True, None]
    
            
def checkPair (AllCards:list)->list:
    result = xOfaKind(AllCards,2)
    
    return result

def checkTwoPair(allCards:list)->list:
    temp = allCards.copy()
    result = xOfaKind(temp,2)
    
    if result[0] == True:
        

        index = [] 
        for i in range(len(temp)):
            if temp[i][1] == result[1][0]:
                index.append(i)

        
        del temp[index[1]]
        del temp[index[0]]
        
       
        result1 = xOfaKind(temp,2)
        
        if result1[0] == True:
        

            return [True,result,result1]
    return [False,None,None]

def checkFullHouse(allCards:list)->list:
    temp = allCards
    result = xOfaKind(temp,3)
    
    if result[0] == True:
        

        index = [] 
        for i in range(len(temp)):
            if temp[i][1] == result[1][0]:
                index.append(i)

       
        del temp[index[2]]
        del temp[index[1]]
        del temp[index[0]]
        
       
        result1 = xOfaKind(temp,2)
        
        if result1[0] == True:
        

            return [True,result,result1]
    return [False,None,None]
        
        


def sortValuesandNumerize(cards) -> list:
    values =[]
    for i in range(len(cards)):
        values.append(cards[i][1])

    sortedValues = values
            
    for i in range(len(sortedValues)):
        if sortedValues[i] == "J":
            sortedValues[i]  = "11"
        elif sortedValues[i] == "Q":
            sortedValues[i]  = "12"
        elif sortedValues[i] == "K":
            sortedValues[i]  = "13"
        elif sortedValues[i] == "A":
            sortedValues[i]  = "1"
            sortedValues.append("14")
        elif sortedValues[i] == "1":
            sortedValues[i]  = "10"

    return sorted(sortedValues)

def xOfaKind(allCards:list, x)->list:
   
    sortedValues = sortValuesandNumerize(allCards)
    
    
    maxCountinaRow = 0
    indexs = []
    #loop through sortedValues that finds if there are 5 consecutive incrementing values
    for i in range(len(sortedValues)-1):
        
        if int(sortedValues[i]) == int(sortedValues[i+1]):
            maxCountinaRow += 1
            indexs.append(i)
        else:
            
            if maxCountinaRow >= x - 1:
                if sortedValues[indexs[0]] == '1':
                    return [True,'A']
                return [True,sortedValues[indexs[0]]]
            maxCountinaRow = 0
            indexs = []
    if maxCountinaRow >= x-1:
            if sortedValues[indexs[0]] == '1':
                    return [True,'A']
            return [True,sortedValues[indexs[0]]]
    return [False,None]
        
        
def checkStraight(allCards:list)->list:
    
    sortedValues = sortValuesandNumerize(allCards)
    final = []
    maxCountinaRow = 0
    indexs = []
    #loop through sortedValues that finds if there are 5 consecutive incrementing values
    for i in range(len(sortedValues)-1):
        if int(sortedValues[i]) + 1 == int(sortedValues[i+1]):
            maxCountinaRow += 1
            indexs.append(i)
        else:
            if maxCountinaRow == 4:
                if sortedValues[indexs[0]] == 1:
                    for i in range(len(indexs)):
                        if sortedValues[indexs[i]] == 1:
                            sortedValues[indexs[i]] == 'A'
                        final.append(sortedValues[indexs[i]])
                    final.append(str(int(final[-1])+1 ))
                    return [True,final]
            maxCountinaRow = 0
            indexs = []
    if maxCountinaRow == 4:
        for i in range(len(indexs)):
            if sortedValues[indexs[i]] == 1:
                sortedValues[indexs[i]] == 'A'
            final.append(sortedValues[indexs[i]])
        final.append(str(int(final[-1])+1 ))
        return [True,final]
    return [False,None]
    

        
def checkFlush(allCards:list)->list:
    suitsInPlay = []
    valuesInPlay =[]
    for i in range(len(allCards)):
        suitsInPlay.append(allCards[i][0])
        valuesInPlay.append(allCards[i][1])
    
    numValues = valuesInPlay

    allSameSuit = []
    suit = None

    for i in range(len(suitsInPlay)):
        if suitsInPlay.count(suitsInPlay[i]) == 5:
            allSameSuit.append(numValues[i])
            suit = suitsInPlay[i]
    
    if suit == None:
        return [False,None, None]
    
    for i in range(len(allSameSuit)):
        if allSameSuit[i] == "J":
            allSameSuit[i]  = "11"
        elif allSameSuit[i] == "Q":
            allSameSuit[i]  = "12"
        elif allSameSuit[i] == "K":
            allSameSuit[i]  = "13"
        elif allSameSuit[i] == "A":
            allSameSuit[i]  = "1"
            allSameSuit.append("14")
        elif allSameSuit[i] == "1":
            allSameSuit[i]  = "10"

        allSameSuit = sorted(allSameSuit)
        if allSameSuit[0] == '1' and allSameSuit[1] != '2':
            return [True, '10', suit]
        elif allSameSuit[0] == '1' and allSameSuit[1] == '2':
            return [True, 'A', suit]
        else:
            return [True, allSameSuit, suit]

    
       
        
    


    










if __name__ == "__main__":

   
    print(checkChances(["♠2","♠4"],["♠3","♣A","♠6","♠5","♣K"]))

    #highcard is 1
    #pair is 2
    #two pair is 3
    #three of a kind is 4
    #straight is 5
    #flush is 6
    #full house is 7
    #four of a kind is 8
    #straight flush is 9
    #royal flush is 10