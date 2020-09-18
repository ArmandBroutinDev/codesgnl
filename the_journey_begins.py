def add(param1, param2):
    return param1+param2

def centuryFromYear(year):
    century = int(year / 100)
    if year % 100 != 0:
        century += 1
    return century

def checkPalindrome(inputString):
    pos = 0
    for i in inputString:
        j = inputString[len(inputString)-1-pos]
        if i != j:
            return False;
        pos+=1
    return True;
