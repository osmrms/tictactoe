'''
=========================================
|  Tic Tac Toe game created by OS-MRMS   |
|              10 Aug 2013               |
| This graphical game created by tkinter |
|               win alg                  |
=========================================
'''
from tkinter import Tk, Button as B, PhotoImage, messagebox as mb
flg = True
a = 0
win = ((0,1,2),
       (3,4,5),
       (6,7,8),
       (0,3,6),
       (1,4,7),
       (2,5,8),
       (0,4,8),
       (2,4,6))
def handler(event):
    global flg, a
    if a == 9:
        for i in b:
            i['text'] = ''
            i['image'] = ''
            i['state'] = 'normal'
        a = 0
        flg = True
def commander(x):
    global flg, a
    if b[x]['text'] == '':
        b[x]['image'] = cir if flg else xir
        b[x]['text'] = 'o' if flg else 'x'
        flg = not flg
        root.iconphoto(False, cir if flg else xir)
        a += 1
    if a == 9:
        for i in b:
            i['state'] = 'disabled'
    win_check()
def win_check():
    temp = []
    global win, a
    j = 10
    for i in b:
        if i['text'] != '':
            temp.append(1 if i['text'] == 'x' else 0)
        else:
            temp.append(j)
            j += 1
    for i in win:
        if temp[i[0]] == temp[i[1]] == temp[i[2]]:
            temp = 'X' if temp[i[0]] == 1 else 'O'
            a = 9
            for i in b:
                i['state'] = 'disabled'
            break
        else:
            if a == 9:
                temp = 'No'
                break
    if 'str' in str(type(temp)):
        if temp != 'No':
            root.iconphoto(False, cir if temp == 'O' else xir)
        else:
            root.iconphoto(False, nowin)
        mb.showinfo('Result', temp + ' win!')
        root.iconphoto(False, cir)
root = Tk()
root.geometry('750x750')
root.title('Tic Tac Toe')
cir = PhotoImage(file = r"cir.png")
xir = PhotoImage(file = r"x.png")
nowin = PhotoImage(file = r"nowin.png")
root.iconphoto(False, cir)
root.resizable(False, False)
b = []
x = [0,0,0,250,250,250,500,500,500]
y = [0,250,500,0,250,500,0,250,500]
for i in range(9):
    b.append(B(root, text = '',
               command = lambda x = i: commander(x),
               width = 250,
               height = 250,
               relief = 'raised'))
    b[i].place(x = x[i], y = y[i])
    b[i].bind('<Button-3>', handler)

root.mainloop()
