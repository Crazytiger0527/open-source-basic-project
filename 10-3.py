from tkinter import *
from tkinter import ttk

window = Tk()

baseTab = ttk.Notebook(window)   # ttk의 탭 컨트롤을 만들어서 윈도우 창에 부착

# 2019038040 나광호

tabDog = ttk.Frame(baseTab)      # 강아지 이름의 탭을 생성 후 추가
baseTab.add(tabDog, text='강아지')  
tabCat = ttk.Frame(baseTab)      # 고양이 이름의 탭을 생성 후 추가
baseTab.add(tabCat, text='고양이')

baseTab.pack(expand=1, fill="both")    # 탭을 화면에 표시

photoDog = PhotoImage(file = "gif/dog7.gif")   # 강아지 그림을 강아지 탭에 부착
labelDog = Label(tabDog, image = photoDog)     
labelDog.pack()

photoCat = PhotoImage(file = "gif/cat5.gif")   # 고양이 그림을 고양이 탭에 부착
labelCat = Label(tabCat, image = photoCat)
labelCat.pack()

window.mainloop()
