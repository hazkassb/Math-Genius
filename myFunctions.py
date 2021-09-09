from random import randint
from os import remove, rename

'''
This function takes a userName as parameter and returns the score for that user if the userName is already in
 our data store, else -1 is returned
'''
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


'''
upsert() --> if the user is new, then username and score are appended to the end of our data store, else we update the user's score
'''
def updateUserPoints(newUser: bool, userName: str, score: str) -> None:
    f = open('userScores.txt', 'a')
    
    if newUser:
        f.write('\n'+userName, score)
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


'''
Generates an algebraic question with 5 operands and 4 operators
'''
def generateQuestions():
    operandList, operatorList = [randint(1, 9) for i in range(0,5)], list()
    operatorDict = dict()
    operatorDict.update({1:'+'})
    operatorDict.update({2:'-'})
    operatorDict.update({3:'*'})
    operatorDict.update({4:'**'})
    print(operandList)
    print(operatorDict)
    prev = ''
    for i in range(0,4):
        curr = operatorDict[randint(1,4)]
        if i > 0:
            prev = operatorList[i-1]
        if prev == '**' and curr == '**':
            continue
        operatorList.append(curr)
        prev = curr
    print(operatorList)
    questionStr = str(operandList[0])
    for i in range(len(operatorList)):
        questionStr += (str(operatorList[i]) + str(operandList[i+1]))
    
    result = eval(questionStr)
    questionStr = questionStr.replace("**", "^")
    print("Evaluate: " + questionStr)
    userInput = input("Type your answer: ")

    while True:
        try:
            userInput = int(userInput)
            break
        except:
            print("please enter a valid numerical answer")
            userInput = input("Type your answer: ")

    if userInput == result:
        print(1)
    else:
        print(0)
    
    return int(result)
