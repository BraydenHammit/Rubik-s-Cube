import copy as c

def rotate(side,ccc,canvas,cube,display,dt):
    cubeT = c.deepcopy(cube)
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
            cube[2][0][0] = cubeT[2][2][0]  #Red from Red
            cube[2][0][1] = cubeT[2][1][0]
            cube[2][0][2] = cubeT[2][0][0]
            cube[2][1][0] = cubeT[2][2][1]
            cube[2][1][2] = cubeT[2][0][1]
            cube[2][2][0] = cubeT[2][2][2]
            cube[2][2][1] = cubeT[2][1][2]
            cube[2][2][2] = cubeT[2][0][2]
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
            cube[2][2][0] = cubeT[2][0][0]  #Red from Red
            cube[2][1][0] = cubeT[2][0][1]
            cube[2][0][0] = cubeT[2][0][2]
            cube[2][2][1] = cubeT[2][1][0]
            cube[2][0][1] = cubeT[2][1][2]
            cube[2][2][2] = cubeT[2][2][0]
            cube[2][1][2] = cubeT[2][2][1]
            cube[2][0][2] = cubeT[2][2][2]

    colors = {
        'W': 'white',
        'R': 'red',
        'G': 'green',
        'Y': 'yellow',
        'O': "#ff7300",
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
                face = 5
            elif face == 3:
                face = 6
        for row in range(3):
            for col in range(3):
                if face == 4:
                    row2 = col
                    col2 = 2 - row
                else:
                    row2 = row
                    col2 = col
                colr = colors[cube[face][row2][col2]]
                if dt == 1:
                    canvas.itemconfig(id[row * 3 + col], fill=colr)
                if dt == 2:
                    canvas.itemconfig(id[row * 3 + col], fill=colr)