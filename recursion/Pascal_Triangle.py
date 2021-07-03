def printPascal(testVariable) :
    if testVariable == 0:
        return [1]
    else:
        firstnum = [1]
        addnum = printPascal(testVariable-1)
        for i in range (len(addnum)-1):
            firstnum.append(addnum[i]+addnum[i+1])
        firstnum +=[1]
    print(firstnum)
    return firstnum

printPascal(3)