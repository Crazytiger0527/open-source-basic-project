# 5주차 과제 4번
import random

def getNumber(Str):   # 문자열을 받아 숫자만 추출하는 함수
    numStr=''    # 숫자만 저장할 문자열 변수 선언
    for ch in Str:  # 글자 수만큼 반복
        if ch.isdigit():  # 글자가 숫자일경우
            numStr += ch   # numStr에 추가

    return int(numStr)  # numStr을 int형으로 리턴

data = []    # 16진수를 받을 리스트
for i in range(0,10):  # 10번 반복
    tmp = hex(random.randrange(0,100000))  # 랜덤으로 16진수 받기
    tmp = tmp[2:]  # 앞에 두개 제거(0x)
    data.append(tmp)   # 리스트에 추가

# 2019038040 나광호

print('정렬 전 데이터 : ', end ='')   # 정렬 전 데이터 출력
[print(num,end=' ')for num in data]

for i in range(0,len(data)-1):     # 선택정렬로 오름차순 정렬
    for k in range(i+1,len(data)):
        if getNumber(data[i])>getNumber(data[k]):   # 16진수 안에 숫자만 취급하여 비교
            data[i], data[k] = data[k], data[i]     # swap

print('\n정렬 후 데이터 : ', end ='')    # 정렬 후 데이터 출력
[print(num,end=' ')for num in data]
