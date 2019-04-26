#이진수를 십진수로! 많이 고민했던 문제죠~

def decimal(binary):
    num = 0
    while binary//10**num >0:   #이진수의 0의 개수를 구하는 것!
        num += 1
    if num == 0:
        return binary
    else:
        ga = num -1
        hap = 2
        for i in range(ga):
            hap = (hap + binary//10**ga - (binary//10**(ga+1))*10)*2
            ga -= 1
