def sumDigits(testVariable):
    if not testVariable:
        return 0
    else:
        return int(testVariable[0])+sumDigits(testVariable[1:])
