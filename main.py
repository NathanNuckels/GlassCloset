from tkinter import *
import time
import math
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
tk.title("Glass Closet - Objects: 2, Clock: 1337")
tick=500
while tick!=0:
	tk.update()
	tk.title("Glass Closet - Objects: 2, Clock: "+str(tick))
	tick-=1
	time.sleep(0.01)
canvas.delete("all")
canvas.create_rectangle(0,0,1280,720,fill="black")
tick=0
tk.title("Glass Closet")
while tick!=255:
	obj=1
	tick+=1
	tmp_color=hex(tick)[2:]
	if len(tmp_color)==1:
		tmp_color="0"+tmp_color
	tmp_color="#"+tmp_color+tmp_color+tmp_color
	canvas.create_rectangle(0,0,1280,720,fill="black")
	canvas.create_text(1280/2,720/2,fill=tmp_color,font=("Helvetica",42),text="Presented by Alan Grey") #Alan Grey is my stage name.
	tk.update()
	time.sleep(0.01)
	canvas.delete("all")
canvas.delete("all")
while tick!=0:
	tick-=1
	tmp_color=hex(tick)[2:]
	if len(tmp_color)==1:
		tmp_color="0"+tmp_color
	tmp_color="#"+tmp_color+tmp_color+tmp_color
	canvas.create_rectangle(0,0,1280,720,fill="black")
	canvas.create_text(1280/2,720/2,fill=tmp_color,font=("Helvetica",42),text="Presented by Alan Grey") #Alan Grey is my stage name.
	tk.update()
	time.sleep(0.01)
	canvas.delete("all")
tt=[
	canvas.create_text(0,360,font=("Helvetica",36),text="B"),
	canvas.create_text(0,360,font=("Helvetica",36),text="r"),
	canvas.create_text(0,360,font=("Helvetica",36),text="e"),
	canvas.create_text(0,360,font=("Helvetica",36),text="a"),
	canvas.create_text(0,360,font=("Helvetica",36),text="k"),
	canvas.create_text(0,360,font=("Helvetica",36),text="t"),
	canvas.create_text(0,360,font=("Helvetica",36),text="h"),
	canvas.create_text(0,360,font=("Helvetica",36),text="r"),
	canvas.create_text(0,360,font=("Helvetica",36),text="o"),
	canvas.create_text(0,360,font=("Helvetica",36),text="u"),
	canvas.create_text(0,360,font=("Helvetica",36),text="g"),
	canvas.create_text(0,360,font=("Helvetica",36),text="h")]

ticks=0
while 1:
	ticks+=1
	tk.update()
	time.sleep(0.01)

