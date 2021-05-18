import tkinter
import random
canvas = tkinter.Canvas(bg= "navy", height=600, width=600)
canvas.pack()

x=random.randint(0,600)
y=random.randint(0,600)

##x=200
##y=300

canvas.create_oval(x, y, x+200, y+200, fill='white', outline='white', width=3)
canvas.create_oval(x+25, y-125, x+175, y+25, fill='white', outline='white', width=3)
canvas.create_oval(x+50, y-200, x+150, y-100, fill='white', outline='white', width=1)

canvas.create_rectangle(x+50, y-210, x+150, y-190, fill='black', outline='black', width=1)
canvas.create_rectangle(x+70, y-210, x+130, y-270, fill='black', outline='black', width=1)
canvas.create_rectangle(x+70, y-220, x+130, y-210, fill='red', outline='red', width=1)

canvas.create_line(x+100, y-135, x+100, y-155, x+50, y-135, x+100, y-135, fill="orange", width=10)

canvas.create_oval(x+75, y-175, x+85, y-165, fill="black", outline="black", width=1)
canvas.create_oval(x+125, y-175, x+115, y-165, fill="black", outline="black", width=1)

canvas.create_oval(x+95, y-85, x+105, y-75, fill='black', outline='black', width=1)
canvas.create_oval(x+95, y-55, x+105, y-45, fill='black', outline='black', width=1)
canvas.create_oval(x+95, y-25, x+105, y-15, fill='black', outline='black', width=1)
canvas.create_oval(x+95, y+5, x+105, y+15, fill='black', outline='black', width=1)
canvas.create_oval(x+95, y+35, x+105, y+45, fill='black', outline='black', width=1)
canvas.create_oval(x+95, y+65, x+105, y+75, fill='black', outline='black', width=1)
canvas.create_oval(x+95, y+95, x+105, y+105, fill='black', outline='black', width=1)
canvas.create_oval(x+95, y+125, x+105, y+135, fill='black', outline='black', width=1)
canvas.create_oval(x+95, y+155, x+105, y+165, fill='black', outline='black', width=1)

canvas.create_oval(x, y-100, x+50, y-50, fill='white', outline='white', width=3)
canvas.create_oval(x+150, y-100, x+200, y-50, fill='white', outline='white', width=3)
