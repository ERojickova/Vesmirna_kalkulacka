from tkinter import *
from PIL import Image, ImageTk
from math import nan, sqrt

# Vytvoření okna
root = Tk()
root.title("Kalkulačka")
root.iconbitmap('images/icon.ico')

# Zobrazení obrázku na pozadí
bg = PhotoImage(file = "images/vesmir.png")
BgImgLabel = Label(root, image = bg)
BgImgLabel.place(x=0, y=0)

# Uložení obrázků do proměnných 
img_dbz = PhotoImage(file='images/dbz.png')
img_tbr = PhotoImage(file='images/tbr.png')
img_dnp = PhotoImage(file='images/dnp.png')
img_complex = PhotoImage(file='images/complex.png')
img_tpt = PhotoImage(file='images/tpt.png')
img_divide = PhotoImage(file='images/divide.png')
img_zarovka = PhotoImage(file='images/zarovka.png')

# List pro ukládání znaků
char=[]


#Převedení listu na číslo
def CharToOneNumber():
    num = '' 
    for i in range(len(char)):
        num = num + char[i]
    return int(num)

# Převedení čísla na list
def NumberIntoChar(num):
    num = str(num)
    for i in range(len(num)):
        char.append(num[i])
    return char


# Funkce pro jednotlivá tlačítka

# Přidání znaku do input pole
def OnClick(num):
    input.insert(len(input.get()),num)
    char.append(num)

# Smazání posledního znaku
def Clear():
    input.delete(len(input.get()) - 1)
    char.pop()

# Smazání celého vstupního pole
def ClearAll():
    input.delete(0, len(input.get()))
    char.clear()

# Zobrazení nápovědy
def Hint():
    top = Toplevel()
    top.title('Nápověda')
    top.iconbitmap('images/hint.ico')
    label = Label(top, text='Nápověda pro zajímavé výsledky:', font=(16)).pack()
    txt1 = Label(top, text='Pokus o dělení nulou').pack()
    txt2 = Label(top, text="Libovolné dělení").pack()
    txt3 = Label(top, text="Výsledek = 42").pack()
    txt4 = Label(top, text="Pokus o odmocnění záporného čísla").pack()
    txt5 = Label(top, text="Výsledek větší než 10 000").pack()
    txt6 = Label(top, text="2+2").pack()
    quit_btn = Button(top, text="Ukončit nápovědu", command=top.destroy).pack()


# Funkce pro počítání faktoriálu
def OnClickFactorial():
    num = CharToOneNumber()
    char.clear()
    result = 1
    for i in range(1, num+1):
        result = result * i
    if result > 10000:
        Open(img_tbr)
        input.delete(0, len(input.get()))
    else:
        input.delete(0, len(input.get()))
        input.insert(0, result)
        NumberIntoChar(result)


# Funkce pro počítání odmocnin
def OnClickSqrt():
    num = CharToOneNumber()
    char.clear()
    if num < 0:
        Open(img_complex)
        input.delete(0, len(input.get()))
        return
    else:
        result = sqrt(num)
        input.delete(0, len(input.get()))
        input.insert(0, result)
        NumberIntoChar(result)


"""
Funkce pro vypočítání příkladu + podmínky pro speciální výsledky
Specíální výsledky:
    * 42; > 10 000; 2+2; /0; /n; sqrt(n<0)
""" 

def Equal():
    if "/0" in input.get():
        Open(img_dbz)
        input.delete(0, len(input.get()))
    else:
        result = eval(input.get())
        if result == 42:
            Open(img_dnp)
            input.delete(0, len(input.get()))
            input.insert(0, result)
            NumberIntoChar(result)
        elif result > 10000:
            Open(img_tbr)
            input.delete(0, len(input.get()))
        elif char == ['2', '+', '2']:
            Open(img_tpt)
            input.delete(0, len(input.get()))
            input.insert(0, 5)
            NumberIntoChar(result)
        elif '/' in input.get():
            Open(img_divide)
            input.delete(0, len(input.get()))
            input.insert(0, result)
            NumberIntoChar(result)
        else:
            input.delete(0, len(input.get()))
            input.insert(0, result)
            char.clear()
            NumberIntoChar(result)


# Funkce pro otevírání nového okna s obrázkem
def Open(img):
    top = Toplevel()
    label = Label(top, image=img)
    label.pack()
    char.clear()


# Vytvoření rámečku pro lepší responsibilitu
frame = LabelFrame(root, text="Vesmírná kalkulačka", padx=15, pady=15)
frame.pack(padx=10, pady=5)

# Vstupní pole
input = Entry(frame, width=50, borderwidth=5)
input.grid(row=0, column=0, columnspan=3, pady=5)

# šířka a výška tlačítek
x = 8
y = 2

# Vytvoření tlačítek
btn_clear = Button(frame, text='C', command=Clear, width=x, height=y, font=('Arial, 15'))
btn_clearAll = Button(frame, text='AC', command=ClearAll, width=x, height=y, font=("Arial, 15"))
btn_hint = Button(frame, image=img_zarovka, command=Hint)

btn_1 = Button(frame, text='1', command=lambda: OnClick('1'), width=x, height=y, font=('Arial, 15'))
btn_2 = Button(frame, text='2', command=lambda: OnClick('2'), width=x, height=y, font=('Arial, 15'))
btn_3 = Button(frame, text='3', command=lambda: OnClick('3'), width=x, height=y, font=('Arial, 15'))

btn_4 = Button(frame, text='4', command=lambda: OnClick('4'), width=x, height=y, font=('Arial, 15'))
btn_5 = Button(frame, text='5', command=lambda: OnClick('5'), width=x, height=y, font=('Arial, 15'))
btn_6 = Button(frame, text='6', command=lambda: OnClick('6'), width=x, height=y, font=('Arial, 15'))

btn_7 = Button(frame, text='7', command=lambda: OnClick('7'), width=x, height=y, font=('Arial, 15'))
btn_8 = Button(frame, text='8', command=lambda: OnClick('8'), width=x, height=y, font=('Arial, 15'))
btn_9 = Button(frame, text='9', command=lambda: OnClick('9'), width=x, height=y, font=('Arial, 15'))

btn_0 = Button(frame, text='0', command=lambda: OnClick('0'), width=x, height=y, font=('Arial, 15'))
btn_plus = Button(frame, text='+', command=lambda: OnClick('+'), width=x, height=y, font=('Arial, 15'))
btn_minus = Button(frame, text='-', command=lambda: OnClick('-'), width=x, height=y, font=('Arial, 15'))

btn_mul = Button(frame, text='*', command=lambda: OnClick('*'), width=x, height=y, font=('Arial, 15'))
btn_div = Button(frame, text='/', command=lambda: OnClick('/'), width=x, height=y, font=('Arial, 15'))
btn_factorial = Button(frame, text='!', command=OnClickFactorial, width=x, height=y, font=('Arial, 15'))
btn_sqrt = Button(frame, text="√", command=OnClickSqrt, width=x, height=y, font=('Arial, 15'))

btn_equal = Button(frame, text='=', command=Equal, width=x, height=5, font=('Arial, 15'))


# Zobrazení tlačítek
btn_clear.grid(row=1, column=0)
btn_clearAll.grid(row=1, column=1)
btn_hint.grid(row=1, column=2)

btn_9.grid(row=2, column=0)
btn_8.grid(row=2, column=1)
btn_7.grid(row=2, column=2)

btn_6.grid(row=3, column=0)
btn_5.grid(row=3, column=1)
btn_4.grid(row=3, column=2)

btn_3.grid(row=4, column=0)
btn_2.grid(row=4, column=1)
btn_1.grid(row=4, column=2)

btn_plus.grid(row=5, column=0)
btn_0.grid(row=5, column=1)
btn_minus.grid(row=5, column=2)

btn_equal.grid(row=6, rowspan=2, column=0)
btn_mul.grid(row=6, column=1)
btn_div.grid(row=6, column=2)

btn_factorial.grid(row=7, column=1)
btn_sqrt.grid(row=7, column=2)

root.mainloop()