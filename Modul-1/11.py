def apakahkabisat(c):
    if(c%400==0):
        return True
    if(c%100==0):
        return False
    if(c%4==0):
        return True
    return False
print(apakahkabisat(100))
