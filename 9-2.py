from time import*
from datetime import*

def countDays(date1,date2):      #두 날짜 사이의 날짜 수를 세는 함수
    retDays = 0
    year,month,day = date1.split('/')   # /로 연 월 일 분리
    sDay = date(int(year),int(month),int(day))  # 날짜 객체 생성(입력 받은 날)
    year,month,day = date2.split('/')   # /로 연 월 일 분리
    eDay = date(int(year),int(month),int(day))  # 날짜 객체 생성(오늘)
    diffDays = eDay - sDay   # 날짜 차이 계산(오늘-입력 받은 날)
    retDays = diffDays.days  # 날짜 차이를 일수로 저장
    return retDays           # 계산한 날짜 차이 일수를 반환

def getDay(t):      # 요일을 계산해주는 함수
    weeks = ['월','화','수','목','금','토','일']   # 리스트 생성
    return weeks[t.tm_wday]     # 해당 요일을 추출해서 반환

# 2019038040 나광호

startDate = input('시작 날짜(연/월/일) --> ')  # 날짜 입력받기
tm = localtime()    # tm에 오늘 날짜 저장
curDate = str(tm.tm_year) + '/' + str(tm.tm_mon) + '/' + str(tm.tm_mday)  # 오늘 날짜를 연/월/일 형식으로 추출

print(startDate,'부터 오늘(',curDate,')까지는',countDays(startDate,curDate),'일이 지났습니다')  # countDays 함수를 이용하여 입력날과 오늘의 날짜수 차이를 출력
print('그리고 오늘은',getDay(tm),'요일입니다')   # getDay함수를 이용하여 오늘 요일을 출력

