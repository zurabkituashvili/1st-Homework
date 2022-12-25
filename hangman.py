from random import randint# Do not delete this line

def displayIntro():
    file = open("intro.txt", "r")
    intro = file.read()
    print(intro)

def displayEnd(result):
    if result == True:
        fileWinner = open("winner.txt", "r")
        end = fileWinner.read()
        print(end)
    else:
        fileLoser = open("loser.txt", "r")
        end = fileLoser.read()
        print(end)

def displayHangman(state):
    firstStage = open("firststage.txt", "r")
    stage1 = firstStage.read()
    socondStage = open("secondtstage.txt", "r")
    stage2 = socondStage.read()
    thirdStage = open("thirdtstage.txt", "r")
    stage3 = thirdStage.read()
    fourthStage = open("fourthstage.txt", "r")
    stage4 = fourthStage.read()
    fifthStage = open("fifthstage.txt", "r")
    stage5 = fifthStage.read()
    sixthStage = open("sixthstage.txt", "r")
    stage6 = sixthStage.read()

    if state == 5:
        print(stage1)
    elif state == 4:
        print(stage2)
    elif state == 3:
        print(stage3)
    elif state == 2:
        print(stage4)
    elif state == 1:
        print(stage5)
    elif state == 0:
        print(stage6)


def getWord():    
    words = open("hangman-words.txt", "r")
    randomWord = words.readlines()
    randWord1 = randomWord[randint(0, 852)].replace('\n', '')
    return(randWord1)

def valid(c):
    if c.isalpha() and len(c) == 1 and c.islower():
        return True
    else:
        return False


def play():
    underscoreNumber = []
    randWord = getWord()
    for i in range(len(randWord)):
        underscoreNumber.append('_')
    state = 5

    while True:
        displayHangman(state)
        if state == 0:
            print('Hidden word was:  ' + randWord)
            return False


        print("Guess the word:  " + ''.join(underscoreNumber))  
        c = input("enter the letter:  ")
        was_present = False
        if valid(c):
            for i in range(len(randWord)):
                if c == randWord[i]:
                    underscoreNumber[i] = c
                    was_present = True
        else:
            continue
        if was_present == False:
            state = state - 1         
                    
        if ''.join(underscoreNumber)==randWord:
            print('Hidden word was:  ' + randWord)
            return True

   

    
def hangman():
    while True:
        displayIntro()
        result = play()
        displayEnd(result)
        print('Do you want to play again? (yes/no)')
        looper = input()
        if looper == 'yes':
            continue
        elif looper == 'no':
            break
        

if __name__ == "__main__":
    hangman()