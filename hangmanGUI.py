import tkinter
import customtkinter
import turtle
from random_word import RandomWords
root_tk = customtkinter.CTk()  
customtkinter.set_default_color_theme("green")
root_tk.geometry("1000x650")
root_tk.config(bg='#ecebc9')
root_tk.resizable(0, 0)
root_tk.title('Hangman')
c = customtkinter.CTkCanvas(root_tk, bg="beige", height=440, width=375)
c.place(x=75, y=75)
randomdic = RandomWords()
word = randomdic.get_random_word()
makeguessempty = ''
for letters in word: 
    makeguessempty += '_ '
operation = 1
def checklet(letter):
    global operation
    global makeguessempty
    for i in range(len(word)):
        if word[i] == letter:
            makeguessempty = makeguessempty[:2*i] + letter + makeguessempty[2*i+1:]
    guessword.configure(text=makeguessempty)
    if '_ ' not in makeguessempty:
        c.create_text(116,409,text="You Win!", fill="#2ea472", font=('Helvetica 20 '))
        c.place()
        for x in (A, B, C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z):
            x.configure(state = 'disabled')
    if letter not in makeguessempty:
        if operation == 1:
            c.create_oval(127, 14, 234, 114, width=3, outline='#2ea472')
        if operation == 2:
            c.create_line(177,115,177,250,width=3, fill='#2ea472')
        if operation == 3:
            c.create_line(177,141,97,213,width=3, fill='#2ea472')
        if operation == 4:
            c.create_line(177,141,256,213,width=3, fill='#2ea472')
        if operation == 5:
            c.create_line(177,250,104,351,width=3, fill='#2ea472')
        if operation == 6:
            c.create_line(177,250,236,351,width=3, fill='#2ea472')
        if operation == 7:
            c.create_text(116,409,text="Game Over!", fill="#2ea472", font=('Helvetica 20 '))
            c.place()
            for x in (A, B, C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z):
                x.configure(state = 'disabled')
            guessword.configure(text=word)            
        operation +=1

guessword = customtkinter.CTkLabel(root_tk, text='', bg_color='#ecebc9', text_color = '#000000', font=('Times New Roman', 26))
guessword.place(x = 200, y = 585)
guessword.configure(text = makeguessempty)


A = customtkinter.CTkButton(root_tk, text= "A" , corner_radius = 150, bg_color='#ecebc9', command=lambda:[checklet('a'),A.configure(state="disabled")])
A.configure(height = 30, width = 30)
A.place(x=670, y=75)

B = customtkinter.CTkButton(root_tk, text= "B" , corner_radius = 150, bg_color='#ecebc9',command=lambda: [checklet('b') ,B.configure(state="disabled")] )
B.configure(height = 30, width = 30)
B.place(x=740, y=75)

C = customtkinter.CTkButton(root_tk, text= "C" , corner_radius = 150, bg_color='#ecebc9',command=lambda: [checklet('c'),C.configure(state="disabled")])
C.configure(height = 30, width = 30)
C.place(x=810, y=75)

D = customtkinter.CTkButton(root_tk, text= "D" , corner_radius = 150, bg_color='#ecebc9',command=lambda: [checklet('d'),D.configure(state="disabled")])
D.configure(height = 30, width = 30)
D.place(x=880, y=75)

E = customtkinter.CTkButton(root_tk, text= "E" , corner_radius = 150, bg_color='#ecebc9',command=lambda: [checklet('e'),E.configure(state="disabled")])
E.configure(height = 30, width = 30)
E.place(x=670, y=145)

F = customtkinter.CTkButton(root_tk, text= "F" , corner_radius = 150, bg_color='#ecebc9',command=lambda: [checklet('f'),F.configure(state="disabled")])
F.configure(height = 30, width = 30)
F.place(x=740, y=145)

G = customtkinter.CTkButton(root_tk, text= "G" , corner_radius = 150, bg_color='#ecebc9',command=lambda: [checklet('g'),G.configure(state="disabled")])
G.configure(height = 30, width = 30)
G.place(x=810, y=145)

H = customtkinter.CTkButton(root_tk, text= "H" , corner_radius = 150, bg_color='#ecebc9',command=lambda: [checklet('h'),H.configure(state="disabled")])
H.configure(height = 30, width = 30)
H.place(x=880, y=145)

I = customtkinter.CTkButton(root_tk, text= "I" , corner_radius = 150, bg_color='#ecebc9',command=lambda: [checklet('i'),I.configure(state="disabled")])
I.configure(height = 30, width = 30)
I.place(x=670, y=215)

J = customtkinter.CTkButton(root_tk, text= "J" , corner_radius = 150, bg_color='#ecebc9',command=lambda: [checklet('j'),J.configure(state="disabled")])
J.configure(height = 30, width = 30)
J.place(x=740, y=215)

K = customtkinter.CTkButton(root_tk, text= "K" , corner_radius = 150, bg_color='#ecebc9',command=lambda: [checklet('k'),K.configure(state="disabled")])
K.configure(height = 30, width = 30)
K.place(x=810, y=215)

L = customtkinter.CTkButton(root_tk, text= "L" , corner_radius = 150, bg_color='#ecebc9',command=lambda: [checklet('l'),L.configure(state="disabled")])
L.configure(height = 30, width = 30)
L.place(x=880, y=215)

M = customtkinter.CTkButton(root_tk, text= "M" , corner_radius = 150, bg_color='#ecebc9',command=lambda: [checklet('m'),M.configure(state="disabled")])
M.configure(height = 30, width = 30)
M.place(x=670, y=280)

N = customtkinter.CTkButton(root_tk, text= "N" , corner_radius = 150, bg_color='#ecebc9',command=lambda: [checklet('n'),N.configure(state="disabled")])
N.configure(height = 30, width = 30)
N.place(x=740, y=280)

O = customtkinter.CTkButton(root_tk, text= "O" , corner_radius = 150, bg_color='#ecebc9',command=lambda: [checklet('o'),O.configure(state="disabled")])
O.configure(height = 30, width = 30)
O.place(x=810, y=280)

P = customtkinter.CTkButton(root_tk, text= "P" , corner_radius = 150, bg_color='#ecebc9',command=lambda: [checklet('p'),P.configure(state="disabled")])
P.configure(height = 30, width = 30)
P.place(x=880, y=280)

Q = customtkinter.CTkButton(root_tk, text= "Q" , corner_radius = 150, bg_color='#ecebc9',command=lambda: [checklet('q'),Q.configure(state="disabled")])
Q.configure(height = 30, width = 30)
Q.place(x=670, y=350)

R = customtkinter.CTkButton(root_tk, text= "R" , corner_radius = 150, bg_color='#ecebc9',command=lambda: [checklet('r'),R.configure(state="disabled")])
R.configure(height = 30, width = 30)
R.place(x=740, y=350)

S = customtkinter.CTkButton(root_tk, text= "S" , corner_radius = 150, bg_color='#ecebc9',command=lambda: [checklet('s'),S.configure(state="disabled")])
S.configure(height = 30, width = 30)
S.place(x=810, y=350)

T = customtkinter.CTkButton(root_tk, text= "T" , corner_radius = 150, bg_color='#ecebc9',command=lambda: [checklet('t'),T.configure(state="disabled")])
T.configure(height = 30, width = 30)
T.place(x=880, y=350)

U = customtkinter.CTkButton(root_tk, text= "U" , corner_radius = 150, bg_color='#ecebc9',command=lambda: [checklet('u'),U.configure(state="disabled")])
U.configure(height = 30, width = 30)
U.place(x=670, y=420)

V = customtkinter.CTkButton(root_tk, text= "V" , corner_radius = 150, bg_color='#ecebc9',command=lambda: [checklet('v'),V.configure(state="disabled")])
V.configure(height = 30, width = 30)
V.place(x=740, y=420)

W = customtkinter.CTkButton(root_tk, text= "W" , corner_radius = 150, bg_color='#ecebc9',command=lambda: [checklet('w'),W.configure(state="disabled")])
W.configure(height = 30, width = 30)
W.place(x=810, y=420)

X = customtkinter.CTkButton(root_tk, text= "X" , corner_radius = 150, bg_color='#ecebc9',command=lambda: [checklet('x'),X.configure(state="disabled")])
X.configure(height = 30, width = 30)
X.place(x=880, y=420)

Y = customtkinter.CTkButton(root_tk, text= "Y" , corner_radius = 150, bg_color='#ecebc9',command=lambda: [checklet('y'),Y.configure(state="disabled")])
Y.configure(height = 30, width = 30)
Y.place(x=810, y=490)

Z = customtkinter.CTkButton(root_tk, text= "Z" , corner_radius = 150, bg_color='#ecebc9',command=lambda: [checklet('z'),Z.configure(state="disabled")])
Z.configure(height = 30, width = 30)
Z.place(x=880, y=490)


exitb = customtkinter.CTkButton(root_tk, text= "Exit" , corner_radius = 150, bg_color='#ecebc9', command=root_tk.destroy)
exitb.configure(height = 35, width=120) 
exitb.place(x=670, y=490)

text = customtkinter.CTkLabel(root_tk, text="Your word is:", bg_color='#ecebc9', text_color = '#000000', font=('Times New Roman', 28))
text.place(x = 200, y = 530)


root_tk.mainloop()