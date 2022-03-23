import operator

trainTupleList = [('Tomas',5),('Henry',8),('Adward',9),('Emily',5),
                  ('Tomas',4),('Henry',7),('Tomas',3),('Emily',8),
                  ('Pursh',5),('Goden',13)]                            # 기차명과 수송량이 기록된 튜플의 리스트 준비
tmpTup = None      # 튜플 저장할 tmpTup 선언 후 초기화
trainDic = {}      # 딕셔너리 저장할 trainDic 선언 후 초기화
trainList = []     # 리스트 저장할 trainList 선언 후 초기
currentRank, totalRank = 1,1          # 현재 순위, 최종 순위 저장할 변수 선언 후 1로 초기화
for tmpTup in trainTupleList:         # 딕셔너리로 만들기
    tName = tmpTup[0]                 # tName에 기치명 저장
    tWeight = tmpTup[1]               # tWeight에 무게 저장
    if tName in trainDic:             # 딕셔너리 안에 동일한 기차명이 있다면(key값은 중복되면 안되기 때문)
        trainDic[tName] += tWeight    # value값에 무게 더하기
    else:
        trainDic[tName] = tWeight     # value에 무게 저장

print('기차 수송량 목록 ==> ', trainTupleList)   #trainTupleList 출력
print('-----------------------------')

# 2019038040 나광호

trainList = sorted(trainDic.items(),key=operator.itemgetter(1),reverse = True)  # 딕셔너리(trainDic)의 value와 key를 value를 기준으로 내림차순으로 리스트(trainList)에 정렬한다.
                                                                                # 튜플의 리스트가 됨

print('%-7s'%'기차','%-7s'%'총 수송량','%-7s'%'순위')                        
print('-----------------------------')
print('%-10s' % trainList[0][0],'%-10s'%trainList[0][1],'%-10s'% currentRank)   # 첫번째 기차(1등)출력
for i in range(1,len(trainList)):
    totalRank+=1             # 최종 순위 +1을 한후
    if trainList[i][1] == trainList[i-1][1]:   #총 수송량이 같다면
        pass                 # 넘어감
    else: 
        currentRank=totalRank   # 다르다면 현재 순위에 최종 순위 저장
    print('%-10s' % trainList[i][0],'%-10s' % trainList[i][1],'%-10s' % currentRank) # 차례대로 출력
