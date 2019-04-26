#1. 두수를 입력받아 그 사이의 모든 수의 합을 구하는 함수를 만들자!

def get_sum(a,b):
    sum = 0
    if a > b:
        for i in range (b,a+1):
            sum += i
    else:
        for i in range(a,b+1):
            sum += i
    return sum

print('두정수를 입력해주세요')
a = int(input('정수 1 :'))
b = int(input('정수 2 :'))

print(get_sum(a,b))
