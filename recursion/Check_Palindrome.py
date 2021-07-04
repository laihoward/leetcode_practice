def isPalindrome(testVariable) :
    if not testVariable :
        return True
    elif len(testVariable)==1:
        return True
    elif testVariable[0]==testVariable[-1]:
        return isPalindrome(testVariable[1:-1])
    else:
        return False
