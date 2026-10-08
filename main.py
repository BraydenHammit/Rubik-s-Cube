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
root.geometry('600x400')
canvas = tk.Canvas(root)
display = rectangles(canvas)
canvas.create_window(45, 90, window=tk.Button(root, text="<", width=1, height=1, bg='gray40', activebackground='gray30', font=(None, 10), command=lambda: rotate(1, canvas, cube, display, dt)))
canvas.create_window(275, 90, window=tk.Button(root, text=">", width=1, height=1, bg='gray40', activebackground='gray30', font=(None, 10), command=lambda: rotate(2, canvas, cube, display, dt)))
canvas.create_window(45, 150, window=tk.Button(root, text="<", width=1, height=1, bg='gray40', activebackground='gray30', font=(None, 10), command=lambda: rotate(8, canvas, cube, display, dt)))
canvas.create_window(275, 150, window=tk.Button(root, text=">", width=1, height=1, bg='gray40', activebackground='gray30', font=(None, 10), command=lambda: rotate(7, canvas, cube, display, dt)))

dt = 1
switchbutton = tk.Button(root, text="Flip", command=lambda: dtswitch())
shufflebutton = tk.Button(root, text='Shuffle', command=lambda: shuffle())

canvas.pack(pady=10)
switchbutton.pack(pady=10)
shufflebutton.pack(pady=10)

def dtswitch():
    global dt
    if dt == 1:
        dt = 2
    elif dt == 2:
        dt = 1
    rotate(None,canvas,cube,display,dt)

def shuffle():
    for _ in range(100):
        rotate(0,canvas,cube,display,dt,shuffle=[ran.randint(1, 6), ran.choice(['c', 'cc'])])

rotate(None,canvas,cube,display,dt)
root.mainloop()