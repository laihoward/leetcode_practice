def sort(testVariable, length) :
    if len(testVariable)>1:
        middleP = 1+(length-1)//2
        arrayL = testVariable[:middleP]
        arrayR = testVariable[middleP:]
        sort(arrayL,len(arrayL))
        sort(arrayR,len(arrayR))

        i=j=k = 0
        while i<len(arrayL) and j<len(arrayR):
            if arrayL[i]<=arrayR[j]:
                testVariable[k]=arrayL[i]
                i+=1
            else:
                testVariable[k]=arrayR[j]
                j+=1
            k+=1

        while i<len(arrayL):
            testVariable[k]=arrayL[i]
            i+=1
            k +=1

        while j<len(arrayR):
            testVariable[k]=arrayR[j]
            j+=1
            k +=1
    return testVariable