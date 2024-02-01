from tkinter import *


def clear():

    global equation_text
    equation_label.set('')
    equation_text = ''


def button_press(num):
    global equation_text
    equation_text = equation_text + str(num)
    equation_label.set(equation_text)


def equals():
    global equation_text

    try:
        total = str(eval(equation_text))
        equation_label.set(total)
        equation_text = total
    except ZeroDivisionError:
        equation_label.set('arithmetic error')
        equation_text = ''
    except SyntaxError:
        equation_label.set('Syntax error')
        equation_text = ''


window = Tk()
window.title('Calculator Program')
window.geometry('450x600')
window.config(bg='black')

equation_text = ''

equation_label = StringVar()
label = Label(window, textvariable=equation_label, font=('consoles', 20), bg='white', width=27, height=2)
label.pack()
frame = Frame(window)
frame.pack()

button1 = Button(frame, text=1, bg='grey', activebackground='white', height=4, width=9, font=30,
                 command=lambda: button_press(1))
button1.grid(row=0, column=0)

button2 = Button(frame, text=2, bg='grey', activebackground='white', height=4, width=9, font=30,
                 command=lambda: button_press(2))
button2.grid(row=0, column=1)

button3 = Button(frame, text=3, bg='grey', activebackground='white', height=4, width=9, font=30,
                 command=lambda: button_press(3))
button3.grid(row=0, column=2)

button4 = Button(frame, text=4, bg='grey', activebackground='white', height=4, width=9, font=30,
                 command=lambda: button_press(4))
button4.grid(row=1, column=0)

button5 = Button(frame, text=5, bg='grey', activebackground='white', height=4, width=9, font=30,
                 command=lambda: button_press(5))
button5.grid(row=1, column=1)

button6 = Button(frame, text=6, bg='grey', activebackground='white', height=4, width=9, font=30,
                 command=lambda: button_press(6))
button6.grid(row=1, column=2)

button7 = Button(frame, text=7, bg='grey', activebackground='white', height=4, width=9, font=30,
                 command=lambda: button_press(7))
button7.grid(row=2, column=0)

button8 = Button(frame, text=8, bg='grey', activebackground='white', height=4, width=9, font=30,
                 command=lambda: button_press(8))
button8.grid(row=2, column=1)

button9 = Button(frame, text=9, bg='grey', activebackground='white', height=4, width=9, font=30,
                 command=lambda: button_press(9))
button9.grid(row=2, column=2)

button0 = Button(frame, text=0, bg='grey', activebackground='white', height=4, width=9, font=30,
                 command=lambda: button_press(0))
button0.grid(row=3, column=0)

plus = Button(frame, text='+', bg='grey', activebackground='white', height=4, width=9, font=30,
              command=lambda: button_press('+'))
plus.grid(row=0, column=3)

minus = Button(frame, text='-', bg='grey', activebackground='white', height=4, width=9, font=30,
               command=lambda: button_press('-'))
minus.grid(row=1, column=3)

multiply = Button(frame, text='*', bg='grey', activebackground='white', height=4, width=9, font=30,
                  command=lambda: button_press('*'))
multiply.grid(row=2, column=3)

divide = Button(frame, text='/', bg='grey', activebackground='white', height=4, width=9, font=30,
                command=lambda: button_press('/'))
divide.grid(row=3, column=3)

equal = Button(frame, text='=', bg='grey', activebackground='white', height=4, width=9, font=30,
               command=equals)
equal.grid(row=3, column=2)

decimal = Button(frame, text='.', bg='grey', activebackground='white', height=4, width=9, font=30,
                 command=lambda: button_press('.'))
decimal.grid(row=3, column=1)

clear = Button(window, text='clear', bg='grey', activebackground='white', height=4, width=9, font=30,
               command=clear)
clear.pack()

window.mainloop()
