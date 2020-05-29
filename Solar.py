from tkinter import *
m = Tk()
m.title('Solar System') 
w = Canvas(m, width=1200, height=800, bg="black")
x0 = 550
x1 = 650
y0 = 350
y1 = 450
oval = w.create_oval(x0, y0, x1, y1, fill="yellow")
w.pack()
m.mainloop() 