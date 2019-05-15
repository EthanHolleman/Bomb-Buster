def simon(lastDigitSerial):
    vowels = set(['a','e','i','o','u','y'])
    lastD = lastDigitSerial.lower()
    colors = ['r','b',]

    strikes = input.("Enter current number of strikes (0-2) ")

    if lastD in vowels:
        #create vowel data structure
        colorDictVowel = {'r' : ['b', 'y', 'g'], 'b' : ['r','g','b'], 'g' : ['y', 'b','y'], 'y' : ['g','r','b']}

        while True:
            answerSeq = ''
            currentSeq = input("Inter the current sequence of colors, first letter only, seperated by spaces")
            currentSeq = currentSeq.lower().split(" ")


            for color in currentSeq:
                answerSeq = answerSeq + " " + (colorDictVowel[color][strikes]) #strikes acts as index to get correct response color

            print("Enter: " + answerSeq)
            cont = input("Type y to continue or any other character if module if completed")

            if cont == 'y':
                break
    else:
        #create consenant data strucuture
        colorDictNot = {'r' : ['b', 'r', 'y'], 'b' : ['y','b','g'], 'g' : ['g', 'y', 'b'], 'y' : ['r', 'g','r']}








    strikes = int(input("Enter number of strikes as number"))
    first = input("Enter the first letter of the color of the first flash")
    first = first.lower()
