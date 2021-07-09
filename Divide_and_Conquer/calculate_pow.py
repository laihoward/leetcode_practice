def powerRecursive(x, y):
    if y == 0:
        return 1
    elif (int(y%2)==0):
        return (powerRecursive(x,int(y/2))*powerRecursive(x,int(y/2)))
    else:
        return (x*powerRecursive(x,int(y/2))*powerRecursive(x,int(y/2)))

def powDivideConquer(x,y):
    temp = 0
    if y == 0:
        return 1
    temp = powDivideConquer(x,y//2)
    if y%2 == 0:
        return temp*temp
    else:
        return x*temp*temp


print(powDivideConquer(2,3))