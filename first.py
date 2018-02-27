from tkinter import *

root = Tk()
root.geometry("500x500")

c= Canvas(root, height=450, width=400, bg="gray")
l= c.create_line(15,15,200,227, width=10)
ll= c.create_line(15,15,1,227, width=10)

ml= c.create_line(315,315,200,227, width=10)
mll= c.create_line(15,15,1,227, width=10)



o = c.create_oval(20,20,10,10,fill="red")

oo = c.create_oval(220,220,120,10,fill="red")


arc = c.create_arc(110,50,240,2210, extent=50, fill="red")

r= c.create_rectangle(320,320,200,200,fill="brown")
c.pack()

root.mainloop()