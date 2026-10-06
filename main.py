import copy
import tkinter as tk
from extra_code.display import rectangles

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
canvas.pack()
dt = 1

def rotate(side,ccc):
    global cube
    cubeT = copy.deepcopy(cube)
    if side == 2:
        if ccc == 'c':
            cube[1][0][2] = cubeT[3][0][2]  #White from Green
            cube[1][1][2] = cubeT[3][1][2]
            cube[1][2][2] = cubeT[3][2][2]
            cube[3][0][2] = cubeT[4][0][2]  #Green from Yellow
            cube[3][1][2] = cubeT[4][1][2]
            cube[3][2][2] = cubeT[4][2][2]
            cube[4][0][2] = cubeT[6][0][2]  #Yellow from Blue
            cube[4][1][2] = cubeT[6][1][2]
            cube[4][2][2] = cubeT[6][2][2]
            cube[6][0][2] = cubeT[1][0][2]  #Blue from White
            cube[6][1][2] = cubeT[1][1][2]
            cube[6][2][2] = cubeT[1][2][2]
            cube[2] = [list(row) for row in zip(*cubeT[2][::-1])]
        if ccc == 'cc':
            cube[3][0][2] = cubeT[1][0][2]  #Green from White
            cube[3][1][2] = cubeT[1][1][2]
            cube[3][2][2] = cubeT[1][2][2]
            cube[4][0][2] = cubeT[3][0][2]  #Yellow from Green
            cube[4][1][2] = cubeT[3][1][2]
            cube[4][2][2] = cubeT[3][2][2]
            cube[6][0][2] = cubeT[4][0][2]  #Blue from Yellow
            cube[6][1][2] = cubeT[4][1][2]
            cube[6][2][2] = cubeT[4][2][2]
            cube[1][0][2] = cubeT[6][0][2]  #White from Blue
            cube[1][1][2] = cubeT[6][1][2]
            cube[1][2][2] = cubeT[6][2][2]
            cube[2] = [list(row) for row in zip(*cubeT[2])][::-1]

    colors = {
        'W': 'white',
        'R': 'red',
        'G': 'green',
        'Y': 'yellow',
        'O': 'orange',
        'B': 'blue'
    }
    for face, id in display.items():
        if dt == 1:
            if face == 2:
                face = 3
            elif face == 3:
                face = 2
        if dt == 2:
            if face == 1:
                face = 4
            elif face == 2:
                face = 6
            elif face == 3:
                face = 5
        for row in range(3):
            for col in range(3):
                source_col = 2 - col if dt == 2 else col
                colr = colors[cube[face][row][source_col]]
                canvas.itemconfig(id[row * 3 + col], fill=colr)


def dtswitch():
    global dt
    if dt == 1:
        dt = 2
    elif dt == 2:
        dt = 1
    rotate(None,None)

rotate(None,None)
root.bind('<q>', lambda event:rotate(2, 'cc'))
root.bind('<w>', lambda event:rotate(2, 'c'))
root.bind('<space>', lambda event: dtswitch())
root.mainloop()