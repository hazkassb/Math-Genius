from random import randint
from os import remove, rename


def getUserPoint(userName: str) -> str:
    f, line = None, ''
    try:
       f = open('userScores.txt', 'r')
    except IOError:
        print('File userScores.txt does not exit, but is being created now.')
        f = open('userScores.txt', 'w')
    
    line = f.readline()
    while len(line) != 0:
            record = line.split(", ")
            if line[0] == userName:
                f.close()
                return line[1]
            line = f.readline()

    f.close()
    return '-1'


def updateUserPoints(newUser: bool, userName: str, score: str) -> None:
    f = open('userScores.txt', 'a')
    
    if newUser:
        f.write('\nuserName, score')
        f.close()
        return
    
    tmp = open('userScores.tmp', 'w')
    for line in f.readlines.split('\n'):
        if(line.split(', ')[0] == userName):
            continue
        tmp.write('\n'+line)
    f.close()
    tmp.close()
    remove('userScores.txt')
    rename('userScores.tmp', 'userScores.txt')



def generateQuestions():
    operandList, operatorList = list(randint(1, 9) for i in range(5)), list()
    operatorDict = dict({1:'+'}, {2:'-'}, {3:'*'}, {4:'**'})

    prev = ''
    for i in range(4):
        curr = operatorDict.get(randint(1,4))
        if i > 0:
            prev = operatorList[i-1]
        if prev == '**' and curr == '**':
            continue
        operatorList.append(curr)
        prev = curr
    
    questionStr = operandList[0]
    for i in range(len(operatorList)):
        questionStr += operatorList[i] + operandList[i+1]
    
    result = eval(questionStr)
    questionStr = questionStr.replace("**", "^")
    print("Evaluate: " + questionStr)
    userInput = input("Type your answer: ")

    while True:
        try:
            userInput = int(userInput)
        except:
            print("please enter a valid numerical answer")
            userInput = input("Type your answer: ")

    if userInput == result:
        print(1)
    else:
        print(0)
    
    return questionStr
