#4.count_up함수를 작성! 2개의 정수를 받고 2개 정수 사이에 있는 모든 정수를 화면에 출력한다.!

def count_up(a,b):
    if a>b :
        for i in range(b,a+1):
            print(i)
    else:
        for i in range(a,b+1):
            print(i)

print('두개의 정수를 입력해주세요!')
x = int(input('정수 1 :'))
y = int(input('정수 2 :'))

count_up(x,y)
