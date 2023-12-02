import random
import tkinter as tk
from tkinter import messagebox as mb

class Button(tk.Button):
    def __init__(self, is_bomb, number=0):
        self.is_flag = False
        self.text = tk.StringVar()
        self.i = 0
        self.j = 0

        super().__init__(textvariable= self.text, background="grey")
        if is_bomb:
            self.is_bomb = True
        else:
            self.number = number
            self.is_bomb = is_bomb

    def SetText(self, text):
        self.text.set(text)

    def OnRightClick(self, event):
        self.configure(bg="yellow")
        if not self.is_flag:
            self.is_flag = True
            self.text.set("F")
        else:
            self.configure(bg = "grey")
            self.text.set("")
            self.is_flag = False

    def OnLeftClick(self, event):
        if self.number == 0:
            self.configure(bg="white")
            Open_Zeros(i_=self.i, j_=self.j)
        OpenButton(self)


def LossGame():
    mb.showerror(message="Вы проиграли\n Продолжить?")
    global buttons
    buttons = StartGame()

def WinGame():
    mb.showinfo(message="Вы выиграли\n Продолжить?")
    global buttons
    global difficulty
    if difficulty>4:
        difficulty-=1
    buttons = StartGame()

def Chek_Answers():
    for i in range(10):
        for j in range(10):
            if buttons[i][j].is_bomb and buttons[i][j].is_flag:
                continue
            elif not buttons[i][j].is_bomb and not buttons[i][j].is_flag:
                continue
                
            else:
                LossGame()
                return
    WinGame()

def StartGame()-> list[list[Button]]:
    global window
    window.title(f"Сложность: {16 - difficulty}")
    buttons = [[Button(False) for i in range(10)] for j in range(10)]
    for i in range(10):
        for j in range(10):
            buttons[i][j].place(x=j*30,y=i*30, width=30, height=30)
            buttons[i][j].i=i
            buttons[i][j].j=j
            buttons[i][j].bind("<Button-1>", buttons[i][j].OnLeftClick)
            buttons[i][j].bind("<Button-3>", buttons[i][j].OnRightClick)
            rdn = random.Random()
            if rdn.randint(0, difficulty) == 1:
                buttons[i][j].is_bomb = True
    for i in range(10):
        for j in range(10):
            border_i_1 = max(0, i-1)
            border_i_2 = min(10, i+2)
            border_j_1 = max(0, j-1)
            border_j_2 = min(10, j+2)
            for i_ in range(border_i_1, border_i_2):
                for j_ in range(border_j_1, border_j_2):
                    if buttons[i_][j_].is_bomb:
                        buttons[i][j].number+=1
    return buttons


def Open_Zeros(i_, j_):
    for j in range(j_, -1, -1):
        OpenButton(buttons[i_][j])
        if buttons[i_][j].number != 0:
            break
        for i in range(i_, -1, -1):
            OpenButton(buttons[i][j])
            if buttons[i][j].number!=0:
                break
        for i in range(i_, 10, 1):
            OpenButton(buttons[i][j])
            if buttons[i][j].number!=0:
                break
    for j in range(j_, 10, 1):
        OpenButton(buttons[i_][j])
        if buttons[i_][j].number != 0:
            break
        for i in range(i_, -1, -1):
            OpenButton(buttons[i][j])
            if buttons[i][j].number!=0:
                break
        for i in range(i_, 10, 1):
            OpenButton(buttons[i][j])
            if buttons[i][j].number!=0:
                break
def OpenButton(button: Button):
    if button.is_bomb:
        button.text.set("X")
        button.configure(bg="red")
        LossGame()
    else:
        if button.number == 0:
            button.configure(bg="white")
        if button.number == 1:
            button.configure(bg="blue")
        if button.number == 2:
            button.configure(bg="green")
        if button.number > 2:
            button.configure(bg="orange")
        button.text.set(str(button.number))

window = tk.Tk()
window.geometry("300x350")
difficulty = 15
buttons = StartGame()
chek_button = tk.Button(text="Проверить", command=Chek_Answers)
chek_button.place(x = 100, y = 300, width=100, height=50)




window.mainloop()