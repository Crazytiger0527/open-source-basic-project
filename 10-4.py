from tkinter import *
from tkinter.filedialog import *
from tkinter.simpledialog import*

def func_open() :    # 파일 열기 메뉴 선택시 실행되는 함수
    global filename
    filename = askopenfilename(parent = window, filetypes = (("GIF 파일", "*.gif"), ("모든 파일", "*.*"))) # 파일을 선택후 파일명 선언
    photo = PhotoImage(file = filename)   # 레이블에 이미지 표시
    pLabel.configure(image = photo)
    pLabel.image = photo
    
def func_exit() :   # 종료하는 함수
    window.quit()
    window.destroy()

def func_zoom():     # 확대하는 함수
    global value1
    value1 += 1     # value1값 1씩 증가
    photo = PhotoImage(file = filename) 
    photo = photo.zoom(value1,value1)  # 사진 확대
    pLabel.configure(image = photo)
    pLabel.image = photo
    
def func_subsample():  # 축소하는 함수
    global value2    
    value2 += 1     # value2값 1씩 증가
    photo = PhotoImage(file = filename)
    photo = photo.subsample(value2,value2)   # 사진 축소
    pLabel.configure(image = photo)
    pLabel.image = photo

def keyEvent(event):   #축소 확대처리 하는 함수
    global key
    key = event.keysym
    if key == 'Up':    # 화살표 위쪽 누를시
        func_zoom()    # 확대함수 실행
    elif key == 'Down':  # 화살표 아래 누를시
        func_subsample()  # 축소함수 실행


# 2019038040 나광호

key = 0
value1 = 1
value2 = 1 

   
window = Tk()
window.geometry("500x500")     # 윈도우 창 크기 설정
window.title("연습문제")       # 윈도우 이름 설정

photo = PhotoImage()      # 그림 출력을 위한 레이블 준비
pLabel = Label(window, image = photo)
pLabel.pack(expand=1, anchor = CENTER)

mainMenu = Menu(window)      
window.config(menu = mainMenu)
fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label = "파일", menu = fileMenu)    # 파일 만들기
fileMenu.add_command(label = "파일 열기", command = func_open)  # 파일 열기 만들기, 클릭시 func_open함수 실행
fileMenu.add_separator()
fileMenu.add_command(label = "프로그램 종료", command = func_exit)  # 프로그램 종료 만들기, 클릭시 func_exit함수 실행

window.bind("<Key>",keyEvent)  # 키값 누를시 keyEvent 함수 실행

window.mainloop()

