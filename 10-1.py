from tkinter import *

def  myFunc() :          # 선택한 라디오버튼이 이미지를 바꾸도록 설정하는 함수
    if var.get() == 1 :      # 1번 선택시 1번사진
        labelImage.configure(image = photo1)
    elif var.get() == 2 :    # 2번 선택시 2번 사진
        labelImage.configure(image = photo2)
    else :                   # 그외에는 3번 사진
        labelImage.configure(image = photo3)

# 전역변수 선언
var, labelImage = 0, None
photo1, photo2, photo3 = [None]*3

# 2019038040 나광호

window = Tk()  
window.geometry("400x400")   # 윈도창 크기 설정
window.title("애완동물 선택하기")   # 윈도창 이름 설정
labelText = Label(window, text="좋아하는 동물 투표  ", fg = "blue", font = ("궁서체", 20))   # 라벨 설정(파랑색, 궁서체, 크기20) 

var = IntVar()   
rb1 = Radiobutton(window, text = "강아지", variable = var, value = 1)   # 라디오 버튼 1번 선언
rb2 = Radiobutton(window, text = "고양이", variable = var, value = 2)   # 라디오 버튼 2번 선언
rb3 = Radiobutton(window, text = "토끼", variable = var, value = 3)     # 라디오 버튼 3번 선언
buttonOk = Button(window, text = "사진 보기", command = myFunc)         # 버튼 누를 시 myFunc함수 실행

photo1 = PhotoImage(file = "gif/dog3.gif")     # 사진 1 선언(개)
photo2 = PhotoImage(file = "gif/cat.gif")      # 사진 2 선언(고양이)
photo3 = PhotoImage(file = "gif/rabbit.gif")   # 사진 3 선언(토끼)

labelImage = Label(window, width = 200, height = 200, bg = "yellow",  image = None)   # 레이블에 이미지 넣기 , 초기에는 이미지 안보이게 설정

labelText.pack(padx = 5, pady = 5)   # 위젯을 화면에 보이게 설정(x,y간격 설정)
rb1.pack(padx = 5, pady = 5)         # 위젯(라디오1)을 화면에 보이게 설정(x,y간격 설정)
rb2.pack(padx = 5, pady = 5)         # 위젯(라디오2)을 화면에 보이게 설정(x,y간격 설정)
rb3.pack(padx = 5, pady = 5)         # 위젯(라디오3)을 화면에 보이게 설정(x,y간격 설정)
buttonOk.pack(padx = 5, pady = 5)    # 위젯(사진보기 버튼)을 화면에 보이게 설정(x,y간격 설정)
labelImage.pack(padx = 5, pady = 5)  # 위젯을 화면에 보이게 설정(x,y간격 설정)

window.mainloop()
