from tkinter import *
from  math import  *
def axis():
    global scale
    canvas.create_line(500,890,500,10,arrow =LAST)
    canvas.create_line(10, 450, 990, 450, arrow=LAST)
    canvas.create_text(520, 10, text = "y", font = "Arial 24", fill = "green")
    canvas.create_text(980, 430, text="x", font="Arial 24", fill="green")
    for x in range(1,1000//scale-1):
        canvas.create_line(x*scale, 445, x*scale , 455)
        canvas.create_text(x*scale, 460, text=f"{x-1000//scale//2}", font = "Arial 6")
    for y in range(1,900//scale-1):
        canvas.create_line(495,y*scale,  505, y*scale )
        canvas.create_text( 485,y*scale, text=f"{900//scale//2 - y}", font = "Arial 6")

def draw():
    canvas.delete(ALL)
    axis()
    global scale
    points = []
    x = -1000//scale//2+1
    while x < 1000//scale//2:
        y = eval(enter.get())
        points.append(x*scale+500)
        points.append(-y*scale+450)
        x+= 1/scale
    canvas.create_line(points)






w = Tk()

w.geometry("1000x1000")
w.title("Graph drawer")
w["bg"] = "lightblue"

text = Label(w, text = "f(x)=" , font = "Arial 32", fg = "green", bg = "lightblue")
text.grid(row = 0, column = 0)

enter = Entry(w, font = "Arial 18", fg = "green", bg = "lightgreen")
enter.grid(row = 0, column = 1)

button = Button(w, text = "draw" , font = "Arial 24", fg = "green", bg = "lightblue", command =draw)
button.grid(row = 0, column = 2)


canvas = Canvas(w, width = 1000, height = 900,  bg="lightblue")
canvas.grid(row = 1, column=0, columnspan = 3)
scale = 10


axis()

w.mainloop()