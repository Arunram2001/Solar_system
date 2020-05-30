from tkinter import *
from Planet import *
m = Tk()
m.title('Solar System') 
w = Canvas(m, width=1200, height=800, bg="black")
x0 = 550
x1 = 560
y0 = 350
y1 = 360
earth = planet("Earth",1.02,0.98)
earthOrbit = w.create_oval(((x0+x1)/2)-(earth.f+earth.a)*214, (y1+y0)/2 - (earth.b)*214, ((x1+x0)/2)+(earth.a-earth.f)*214, (y1+y0)/2 + (earth.b)*214 , outline="white")
mercury = planet("Mercury",0.47,0.31)
mercuryOrbit = w.create_oval(((x0+x1)/2)-(mercury.f+mercury.a)*214, (y1+y0)/2 - (mercury.b)*214, ((x1+x0)/2)+(mercury.a-mercury.f)*214, (y1+y0)/2 + (mercury.b)*214 , outline="white")
oval = w.create_oval(x0, y0, x1, y1, fill="yellow")
w.pack()
print((x0+x1)/2-(mercury.f-mercury.a)*214, (y1+y0)/2 - (mercury.b)*214, (x1+x0)/2+(mercury.a-mercury.f)*214, (y1+y0)/2 + (mercury.b)*214)
m.mainloop() 