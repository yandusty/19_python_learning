#2. 숫자를 하나씩 증가하는 함수 inc를 만들고 이를 이용하여 count값을 사용자가 원하는 만큼 증가 시켜보자.

#inc
def inc(num,up):
    for i in range (up):
        num += 1
        print(num)

count = int(input('원하는 숫자를 입력해주세요. '))
up = int(input('앞에서 입력한 숫자를 증가시키고 싶은만큼의 숫자를 적어주세요. '))

inc(count,up)
