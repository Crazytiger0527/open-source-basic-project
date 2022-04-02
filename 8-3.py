# 5주차 과제 3번
import turtle
import random
import math
from tkinter.simpledialog import*

swidth,sheight = 500,500
txtSize = 20    # 글자 크기
turn = 2        # 회전할 바퀴 수 

turtle.title('거북이가 나선 모양의 글자쓰기')
turtle.shape('turtle')
turtle.setup(width = swidth + 50, height = sheight+50)
turtle.screensize(swidth,sheight)
turtle.penup()

inStr = askstring('문자열 입력','거북이가 쓸 문자열을 입력')   # inStr에 문자열 입력받기
count = len(inStr)       # 입력받은 문자열의 길이를 저장
angle = 360*turn / count  # 글자 간격 각도
length = 250     # 중심에서의 거리
angle2 = 250     # 각도
length2 = 250/count   # 중심에서의 거리 간격

# 2019038040 나광호

for ch in inStr:     # 글자 끝 까지
 
    length -= length2     # 거리 줄이기 
    angle2 -= angle      # 각도 줄이기
    x = length * math.cos(math.radians(angle2))  # x 좌표
    y = length * math.sin(math.radians(angle2))  # y 좌표
    turtle.goto(x,y)   # 터틀 위치 설정
    r = random.random(); g = random.random(); b = random.random() # r,g, b 랜덤으로 받기
    turtle.pencolor((r,g,b))  # 터틀 색 설정
    turtle.write(ch,font=('맑은고딕',txtSize,'bold'))  # 맑은고딕, 20의 크기, 볼드체로 적기
turtle.done()
