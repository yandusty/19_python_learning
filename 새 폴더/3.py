# 거리를 계산하는 프로그램을 만드시오!

#GET DIST

def get_max(a,b):
    if a>b:
        return a
    else:
        return b

def get_min(a,b):
    if a<b:
        return a
    else:
        return b

x = int(input('수직선에서 출발하고 싶은 지점을 정해주세요'))
y = int(input('수직선에서 도착하고 싶은 지점을 정해주세요'))

dist = get_max(x,y)-get_min(x,y)
print('거리: %d'%dist)
