from tkinter import *
from Planet import *
m = Tk()
m.title('Solar System') 
canvasWidth = 700
canvasHeight = 700
w = Canvas(m, width=canvasWidth, height=canvasHeight, bg="black")

x0 = canvasWidth/2 - planet.distanceLogConvert(0.0045) #0.0045 - radius of sun in AU
x1 = canvasWidth/2 + planet.distanceLogConvert(0.0045)
y0 = canvasHeight/2 - planet.distanceLogConvert(0.0045)
y1 = canvasHeight/2 + planet.distanceLogConvert(0.0045)

planetsArray = []
planetsArray.append(planet("Mercury",0.47,0.31))
planetsArray.append(planet("Venus",0.728,0.718))
planetsArray.append(planet("Earth",1.02,0.98))
planetsArray.append(planet("Mars",1.67,1.38))
planetsArray.append(planet("Jupiter",5.45,4.95))
planetsArray.append(planet("Saturn",10.0,9.02))
planetsArray.append(planet("Uranus",20.1,18.3))
planetsArray.append(planet("Neptune",30.3,30.0))

for i in planetsArray:
    w.create_oval(((x0+x1)/2)-i.distanceLogConvert(i.f+i.a), (y1+y0)/2 - i.distanceLogConvert(i.b), ((x1+x0)/2)+i.distanceLogConvert(i.a-i.f), (y1+y0)/2 + i.distanceLogConvert(i.b) , outline="white")
    #w.create_oval(((x0+x1)/2)-(i.f+i.a)*i.distanceLogConvert(i.ra), (y1+y0)/2 - (i.b)*i.distanceLogConvert(i.ra), ((x1+x0)/2)+(i.a-i.f)*i.distanceLogConvert(i.rp), (y1+y0)/2 + (i.b)*i.distanceLogConvert(i.rp) , outline="white")
    print(((x0+x1)/2)-i.distanceLogConvert(i.f+i.a), (y1+y0)/2 - i.distanceLogConvert(i.b), ((x1+x0)/2)+i.distanceLogConvert(i.a-i.f), (y1+y0)/2 + i.distanceLogConvert(i.b))
oval = w.create_oval(x0, y0, x1, y1, fill="yellow")
w.pack()
m.mainloop() 