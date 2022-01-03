from tkinter import *
import time
tk=Tk()
tk.title("In a glass closet")
canvas=Canvas(tk,width=1280,height=720)
button1=Button(tk,text="BUTTON 1",bg="#007fff",font="bold")
button2=Button(tk,text="BUTTON 2",bg="#ff0000",font="bold")
button3=Button(tk,text="BUTTON 3",bg="#00ff00",font="bold")
button4=Button(tk,text="BUTTON 4",bg="#ff7f00",font="bold")
canvas.grid(row=0,column=0,columnspan=4,sticky=NSEW)
button1.grid(row=1,column=0,sticky=NSEW)
button2.grid(row=1,column=1,sticky=NSEW)
button3.grid(row=1,column=2,sticky=NSEW)
button4.grid(row=1,column=3,sticky=NSEW)

canvas.create_rectangle(0,0,1280,720,fill="black")
canvas.create_text(100,100,anchor=NW,text="Hey hey! Please don't put this in fullscreen.\nIt kinda looks weird",fill="white",font=("Helvetica",24))


while 1:
	tk.update()
	time.sleep(0.01)
# asphalt8+
