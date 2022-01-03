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
ofset=80
canvas.create_rectangle(0,0,1280,720,fill="black")
tt=[
	canvas.create_text(ofset,1000,font=("Helvetica",24),text="B",fill="white"),
	canvas.create_text(ofset+100,1000,font=("Helvetica",24),text="r",fill="white"),
	canvas.create_text(ofset+200,1000,font=("Helvetica",24),text="e",fill="white"),
	canvas.create_text(ofset+300,1000,font=("Helvetica",24),text="a",fill="white"),
	canvas.create_text(ofset+400,1000,font=("Helvetica",24),text="k",fill="white"),
	canvas.create_text(ofset+500,1000,font=("Helvetica",24),text="t",fill="white"),
	canvas.create_text(ofset+600,1000,font=("Helvetica",24),text="h",fill="white"),
	canvas.create_text(ofset+700,1000,font=("Helvetica",24),text="r",fill="white"),
	canvas.create_text(ofset+800,1000,font=("Helvetica",24),text="o",fill="white"),
	canvas.create_text(ofset+900,1000,font=("Helvetica",24),text="u",fill="white"),
	canvas.create_text(ofset+1000,1000,font=("Helvetica",24),text="g",fill="white"),
	canvas.create_text(ofset+1100,1000,font=("Helvetica",24),text="h",fill="white")]

for z in range(11):
	for i in range(40):
		canvas.move(tt[z],0,-16)
		tk.update()
		time.sleep(0.01)

for i in range(128):
	canvas.move(tt[11],0,-5)
	tk.update()
	time.sleep(0.01)

for z in range(100):
	for i in range(12):
		canvas.move(tt[i],0,-5*(12-i))
	tk.update()
	time.sleep(0.01)

for i in range(64):
	col=i*4
	if col==256:
		col=255
	col=hex(col)[2:]
	if len(col)==1:
		col="0"+col
	col="#"+col+col+col
	canvas.create_rectangle(0,0,1280,720,fill=col)
	tk.update()
	time.sleep(0.01)
ticks=0
while 1:
	ticks+=1
	tk.update()
	time.sleep(0.01)

