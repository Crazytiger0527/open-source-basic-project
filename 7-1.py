#선택정렬을 이용하여 16진수 정렬하기
import random

Hex_List = []           #리스트 선언
for i in range(0,10):   #총 10개의 수 랜덤으로 받아서 리스트에 저장
    x=hex(random.randrange(0,100000))
    Hex_List.append(x)

print('정렬 전 데이터 : ', end='')      #정렬 전 데이터 출력
[print(num,end=' ') for num in Hex_List]

# 2019038040 나광호

for a in range(0,len(Hex_List)-1):        #선택정렬 시작(0~8까지 반복)
    min_index = a                         #Hex_List[a]가 최소값이라 가정
    for b in range(a+1,len(Hex_List)):    #1~9까지 반복
        if int(Hex_List[min_index],16) > int(Hex_List[b],16):   #Hex_List[b]가 더 작으면 min_index b로 변경
            min_index = b
    Hex_List[a],Hex_List[min_index] = Hex_List[min_index],Hex_List[a]   #Hex_List[a]와 가장 작은 값 교체

print('\n정렬 후 데이터 : ', end='')      #정렬 후 데이터 출력
[print(num,end=' ') for num in Hex_List]

    
