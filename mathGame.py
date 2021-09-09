import myFunctions as func

try:
    userName = input('Enter your name: ')

    userScore = int(func.getUserPoint(userName))

    newUser = (userScore == - 1)
    if newUser: userScore = 0

    userChoise = 0

    while userChoise != -1:
        userScore += func.generateQuestions()
        
        if input('type -1 to exit the program') == '-1':
            break
    
    func.updateUserPoints(newUser, userName, userScore)
except Exception:
    print('An error has occured, the problem will exit now.' + Exception)
