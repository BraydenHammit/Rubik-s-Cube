import copy
import tkinter as tk

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
canvas = tk.Canvas(root)

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

root.mainloop()