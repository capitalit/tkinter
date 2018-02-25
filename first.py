from tkinter import *
root = Tk()
root.geometry('400x200')
l=Label(root, text="kalkulator")
l.pack(side=TOP)

def buttonFunction():
    print("hello world")

b = Button(root, text="SUMA", command=buttonFunction)
b.pack(side=BOTTOM)

b0 = Button(root, text="0",command=buttonFunction)
b0.pack(side=LEFT)

b1 = Button(root, text="1",command=buttonFunction)
b1.pack(side=LEFT)

b2= Button(root, text="2",command=buttonFunction)
b2.pack(side=LEFT)

b3 = Button(root, text="3", command=buttonFunction)
b3.pack(side=LEFT)

b4 = Button(root, text="4", command=buttonFunction)
b4.pack(side=LEFT)

b5 = Button(root, text="5", command=buttonFunction)
b5.pack(side=LEFT)

b6 = Button(root, text="6", command=buttonFunction)
b6.pack(side=LEFT)

b7 = Button(root, text="7", command=buttonFunction)
b7.pack(side=LEFT)

b8 = Button(root, text="8", command=buttonFunction)
b8.pack(side=LEFT)

b9 = Button(root, text="9", command=buttonFunction)
b9.pack(side=LEFT)

b10 = Button(root, text="+", command=buttonFunction)
b10.pack(side=BOTTOM)

b11 = Button(root, text="-", command=buttonFunction)
b11.pack(side=BOTTOM)

b12 = Button(root, text="*", command=buttonFunction)
b12.pack(side=BOTTOM)

b13 = Button(root, text="/", command=buttonFunction)
b13.pack(side=BOTTOM)

b14 = Button(root, text="=", command=buttonFunction)
b14.pack(side=BOTTOM)
root.mainloop()
#123123

