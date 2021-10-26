def challList():
    chall = []
    for x in range(100):  #loops through the numbers 0 to one hundred
        if x % 7 == 0:  #uses the modulo operator to check divisibility
                        #If the number divided by 7 returns no remainder, then execute the following code:
            chall.append(x)
    for x in range(100,200):
        if x % 8 == 0:
            chall.append(x)
    for x in range(200,300):
        if x % 9 == 0:
            chall.append(x)
    return chall

print(challList())