import random as ran
import tkinter as tk
from extra_code.display import rectangles
from extra_code.rotation import rotate

cube = {
    1: [['W','W','W'],['W','W','W'],['W','W','W']],    
    2: [['R','R','R'],['R','R','R'],['R','R','R']],
    3: [['G','G','G'],['G','G','G'],['G','G','G']],   
    4: [['Y','Y','Y'],['Y','Y','Y'],['Y','Y','Y']],
    5: [['O','O','O'],['O','O','O'],['O','O','O']],
    6: [['B','B','B'],['B','B','B'],['B','B','B']]
}

root = tk.Tk()
root.title("Rubik's Cube")
root.geometry('400x300')
canvas = tk.Canvas(root)
display = rectangles(canvas)
switchbutton = tk.Button(root, text="Flip", command=lambda: dtswitch())
canvas.pack()
switchbutton.pack(pady=10)
dt = 1

def dtswitch():
    global dt
    if dt == 1:
        dt = 2
    elif dt == 2:
        dt = 1
    rotate(None,None,canvas,cube,display,dt)

def shuffle():
    for _ in range(100):
        rotate(ran.randint(1, 6),ran.choice(['c', 'cc']),canvas,cube,display,dt)

rotate(None,None,canvas,cube,display,dt)
root.bind('<q>', lambda event:rotate(2,'cc',canvas,cube,display,dt))
root.bind('<w>', lambda event:rotate(2,'c',canvas,cube,display,dt))
root.mainloop()