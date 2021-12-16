import random
# def randomSelection() a function that's passed nothing:
count = 0
def randomSelection():
    #opens the text file
    randomList = []
#I had an error because I named my file random, so python wasn't importing from the right library
    open("scrabble5.txt", "r")
    with open("scrabble5.txt", "r") as reader:
    # for line in reader:
        for line in reader:
            listsort = line.split()
            randomList.append(listsort)
        compRandWord = random.choice(randomList)
        return compRandWord

def wordSandwich():
    actualWord = randomSelection()
    lowered = actualWord[0]
    firstIndex = lowered.lower()
    print("Welcome To Word SandWich!!!")
    currentSandwich = "Your current sandwich is: "
    print(currentSandwich)
    upperBound = ""
    print("----", upperBound)
    word = ""
    print("-----", word)
    lowerBound = ""
    print("-----",lowerBound)
    usersInput  = input("Give me a five letter word or press q to quit: ")
    # guessCount = 0
    count = 0

    if usersInput == "q":
                    currentSandwich = "The actual word was "
                    print("-----", upperBound)
                    print(firstIndex.upper(quit
                    ))
                    print("-----", lowerBound)
                    print(currentSandwich, firstIndex)
                    return
    else:
        while len(usersInput) != 5:
                print("That's not a five letter word....")
                usersInput = input("Give me a 5 letter word: ")
                # guessCount +=1
        else:
                while usersInput != firstIndex:
                    currentSandwich = "Your current sandwich is: "
                    if len(usersInput) != 5 and usersInput != "q":
                        print("That's not a 5 letter word")
                        usersInput = input("Give me a 5 letter word or press q to quit: ")
                    elif usersInput == "q":
                        currentSandwich = "The actual word was"
                        print(currentSandwich, firstIndex)
                        print(upperBound)
                        firstIndex  = firstIndex.upper()
                        print(firstIndex)
                        print(lowerBound)
                        break

                    else:
                        if len(upperBound) == 0 and usersInput < firstIndex:
                            upperBound = usersInput
                # print(currentSandwich)
                        elif usersInput < firstIndex and usersInput > upperBound:
                            upperBound = usersInput
                
                        elif len(lowerBound) == 0 and usersInput > firstIndex:
                            lowerBound = usersInput
                        elif usersInput > firstIndex and usersInput < lowerBound:
                            lowerBound = usersInput
                        elif len(usersInput) != 5:
                            currentSandwich = "That's not a 5 letter word...."
                            print(currentSandwich)
                        print(upperBound)
                        print(word)
                        print(lowerBound)
                        usersInput = input("Give me a 5 letter word or press q to quit: ")
                        count += 1
                else:
                    print("Your current sandwich is,", usersInput)
                    print("Congratulations! You got the right word. Play me again")
                    print(upperBound)
                    firstIndex.upper()
                    print(firstIndex)
                    print(lowerBound)
wordSandwich()