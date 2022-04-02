# 5주차 과제 2번
import operator

inStr='''내가 그의 이름을 불러주기 전에는 그는 다만 하나의 몸짓에 지나지 않았다.
내가 그의 이름을 불러주었을 때, 그는 내게로 와 꽃이 되었다.
내가 그의 이름을 불러준 것처럼 나의 이 빛깔과 향기에 알맞은 누가 나의 이름을 불러다오.
그에게로 가서 나도 그의 꽃이 되고 싶다.
우리들은 모두 무엇이 되고 싶다.
나는 너에게 너는 나에게 잊혀지지 않는 하나의 눈짓이 되고 싶다.'''
countDic={}       # 딕셔너리를 이용하여 문자와 빈도수 저장
countList=[]      # 딕셔너리를 정렬하여 저장할 리스트 선언

# 2019038040 나광호

for ch in inStr:      # inStr길이 만큼 반복
    if ch>='ㄱ' and ch <= '힣':   # ch(글자)가 한글이면
        if ch in countDic:        # 그 글자(key)가 딕셔너리 안에 존재한다면
            countDic[ch]+=1       # 그 글자(key)의 빈도수(value값) 1 증가
        else:                     # 아니라면
            countDic[ch]=1        # 그 글자(key)의 빈도수(value값) 1 넣기

countList = sorted(countDic.items(),key=operator.itemgetter(1),reverse=True)   # 딕셔너리의 item을 빈도수를 기준으로 내림차순 정렬 후 리스트에 저장

print('원문\n',inStr)       # 원문 출력
print('---------------')
print('문자\t빈도수')       
print('---------------')
for i in range(0,len(countList)):   # 리스트값 출력( 문자, 빈도수)
    print(countList[i][0],'\t',countList[i][1])
