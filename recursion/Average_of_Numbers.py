def average(testVariable, currentIndex = 0) : 
    
    if currentIndex == 0:
        return (testVariable[currentIndex]+average(testVariable, currentIndex+1))/len(testVariable)
    if currentIndex==(len(testVariable)-1):
        return testVariable[currentIndex]
    return (testVariable[currentIndex]+average(testVariable, currentIndex+1))

testVariable = [10, 2, 3, 4, 8, 0] 
currentIndex = 0
print(average(testVariable, currentIndex = 0))
