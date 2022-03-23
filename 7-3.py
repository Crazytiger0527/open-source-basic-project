import turtle
import random
import operator

playTurtles=[]           # 정렬 전 거북이 저장 리스트
sortedTurtles=[]         # 저장 후 거북이 저장 리스트

turtle.title('거북이 리스트 활용(정렬)')
turtle.setup(550,550)
turtle.screensize(500,500)

for i in range(0,5):                   # 총 5마리 받기
    myTurtle=turtle.Turtle('turtle')   # 거북이 모양
    tX=random.randrange(-250,250)      # x,y 좌표 랜덤으로 받기
    tY=random.randrange(-250,250)
    r = random.random(); g = random.random(); b = random.random()   # r,g,b 랜덤으로 받기
    tSize = random.randrange(1,100)/10    # 거북이 크기 랜덤으로 받기
    tAngle = random.randrange(0,360)      # 거북이 각도 랜덤으로 받기
    playTurtles.append([myTurtle,tX,tY,tSize,tAngle,r,g,b])  # 정렬 전 거북이 저장 리스트에 저장하기

sortedTurtles = sorted(playTurtles,key=operator.itemgetter(3),reverse = False)   # 거북이 크기를 기준으로 오름차순 정렬하여 정렬 후 거북이 저장 리스트에 저장하기

# 2019038040 나광호

for index, tList in enumerate(sortedTurtles[0:]):       # enumerate를 이용하여 튜플형태로 index값을 같이 반환받음
    myTurtle = tList[0]                                 # 거북이 모양 설정
    myTurtle.color((tList[5],tList[6],tList[7]))        # 거북이 색 설정
    myTurtle.pencolor((tList[5],tList[6],tList[7]))     # 팬 색 설정
    myTurtle.turtlesize(tList[3])                       # 거북이 크기 설정
    myTurtle.left(tList[4])                             # 거북이 각도 설정
    myTurtle.penup()                                    # 팬 제거
    if index == 0:                       # index가 0이면(처음 거북이면)
        myTurtle.goto(tList[1],tList[2]) # 거북이 위치로 이동
        continue
    myTurtle.goto(sortedTurtles[index-1][1],sortedTurtles[index-1][2])  # 그 외 거북이들은 전 거북이 위치로 이동
        
    myTurtle.pendown()                  # 펜 on
    myTurtle.goto(tList[1],tList[2])    # 거북이 위치로 이동

turtle.done()
