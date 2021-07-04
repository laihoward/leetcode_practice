def recursiveLength(testVariable) : 
    if not testVariable:
        return 0
    else:
        return 1+recursiveLength(testVariable[1:])