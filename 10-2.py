from tkinter import *
from tkinter.colorchooser import *
from tkinter.simpledialog import *

def  mouseClick(event) :    # 마우스 클릭시의 x,y좌표를 저장하는 함수
    global x1, y1
    x1 = event.x    # x좌표 저장
    y1 = event.y    # y좌표 저장

def mouseDrop(event) :     # 마우스 클릭이 끝났을때의 x,y좌표를 저장 후 시작점과 끝점을 연결하는 선을 긋는 함수
    global x1, y1, x2, y2, penWidth, penColor
    x2 = event.x    # x좌표 저장
    y2 = event.y    # y좌표 저장
    canvas.create_line(x1, y1, x2, y2, width = penWidth, fill = penColor)  # 시작점과 끝점 선 긋기

def getColor() :     # 펜 색을 받을 함수
    global penColor
    color = askcolor()
    penColor = color[1]
     
def getWidth() :    # 펜 두께를 설정하는 함수
    global penWidth
    penWidth = askinteger("선 두께", "선 두께(1~10)를 입력하세요", minvalue = 1, maxvalue = 10)

#2019038040 나광호

window = None
canvas = None
x1, y1, x2, y2 = None, None, None, None 
penColor = 'black'
penWidth=5

window=Tk()
window.title("그림판과 비슷한  프로그램")          # 윈도우 창 이름 설정
canvas = Canvas(window, height = 500, width = 500) # 윈도우 창 크기 설정
canvas.bind("<Button-1>", mouseClick)       # 클릭시 mouseClick함수 실행
canvas.bind("<ButtonRelease-1>", mouseDrop) # 드랍시 mouseDrop함수 실행
canvas.pack()
    
mainMenu = Menu(window)       # 메뉴 생성
window.config(menu=mainMenu)  
fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label="설정", menu=fileMenu)   # 메인 메뉴 -> 설정
fileMenu.add_command(label="선 색상 선택", command=getColor)  # 파일 메뉴 -> 선 색상 선택, 클릭시 getColor함수 실행
fileMenu.add_separator()    
fileMenu.add_command(label="선 두께 설정", command=getWidth) # 파일 메뉴 -> 선 두께 설정, 클릭시 getWidth함수 실행

window.mainloop()
