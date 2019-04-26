#data, filter로 filter에 들어간 문자를 data에서 제거한 문자열을 돌려주자!

#get_filtered

def get_filtered(data,filters):
    num = len(data)
    str = ""
    for i in range (num):
        if data[i] not in filters:
            str = str + data[i]
    return str

data = input('문장을 입력해주세요: ')
filters = '!@#$%^&**(":'

print(get_filtered(data,filters))

