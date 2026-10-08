import copy as c

def rotate(btn,canvas,cube,display,dt,shuffle=False):
    side = None
    ccc = None
    if shuffle != False:
        side, ccc = shuffle[0], shuffle[1]
    else:
        if dt==1:
            if btn==1:
                side=1
                ccc = 'c'
            elif btn==2:
                side=1
                ccc = 'cc'
            elif btn==3:
                side=2
                ccc = 'c'
            elif btn==4:
                side=2
                ccc = 'cc'
            elif btn==5:
                side=3
                ccc = 'c'
            elif btn==6:
                side=3
                ccc = 'cc'
            elif btn==7:
                side=4
                ccc = 'c'
            elif btn==8:    
                side=4
                ccc = 'cc'
            elif btn==9:
                side=5
                ccc = 'c'
            elif btn==10:
                side=5
                ccc = 'cc'
            elif btn==11:
                side=6
                ccc = 'c'
            elif btn==12:
                side=6
                ccc = 'cc'
        elif dt==2:
            if btn==1:
                side=4
                ccc = 'c'
            elif btn==2:
                side=4
                ccc = 'cc'
            elif btn==3:
                side=5
                ccc = 'c'
            elif btn==4:
                side=5
                ccc = 'cc'
            elif btn==5:
                side=6
                ccc = 'c'
            elif btn==6:
                side=6
                ccc = 'cc'
            elif btn==7:
                side=1
                ccc = 'c'
            elif btn==8:    
                side=1
                ccc = 'cc'
            elif btn==9:
                side=3
                ccc = 'c'
            elif btn==10:
                side=3
                ccc = 'cc'
            elif btn==11:  
                side=3
                ccc = 'c'
            elif btn==12:
                side=3
                ccc = 'cc'
    cubeT = c.deepcopy(cube)
    if side == 1:
        if ccc == 'c':
            cube[3][0][0] = cubeT[2][0][0]  #Green from Red
            cube[3][0][1] = cubeT[2][0][1]
            cube[3][0][2] = cubeT[2][0][2]

            cube[5][2][0] = cubeT[3][0][2]  #Orange from Green
            cube[5][2][1] = cubeT[3][0][1]
            cube[5][2][2] = cubeT[3][0][0]

            cube[6][2][0] = cubeT[5][2][0]  #Blue from Orange
            cube[6][2][1] = cubeT[5][2][1]
            cube[6][2][2] = cubeT[5][2][2]

            cube[2][0][0] = cubeT[6][2][2]  #Red from Blue
            cube[2][0][1] = cubeT[6][2][1]
            cube[2][0][2] = cubeT[6][2][0]

            cube[1][0][0] = cubeT[1][2][0]  #White from White
            cube[1][0][1] = cubeT[1][1][0]
            cube[1][0][2] = cubeT[1][0][0]
            cube[1][1][0] = cubeT[1][2][1]
            cube[1][1][2] = cubeT[1][0][1]
            cube[1][2][0] = cubeT[1][2][2]
            cube[1][2][1] = cubeT[1][1][2]
            cube[1][2][2] = cubeT[1][0][2]

        if ccc == 'cc':
            cube[2][0][0] = cubeT[3][0][0]  #Red from Green
            cube[2][0][1] = cubeT[3][0][1]
            cube[2][0][2] = cubeT[3][0][2]

            cube[3][0][2] = cubeT[5][2][0]  #Green from Orange
            cube[3][0][1] = cubeT[5][2][1]
            cube[3][0][0] = cubeT[5][2][2]

            cube[5][2][0] = cubeT[6][2][0]  #Orange from Blue
            cube[5][2][1] = cubeT[6][2][1]
            cube[5][2][2] = cubeT[6][2][2]

            cube[6][2][2] = cubeT[2][0][0]  #Blue from Red
            cube[6][2][1] = cubeT[2][0][1]
            cube[6][2][0] = cubeT[2][0][2]

            cube[1][2][0] = cubeT[1][0][0]  #White from White
            cube[1][1][0] = cubeT[1][0][1]
            cube[1][0][0] = cubeT[1][0][2]
            cube[1][2][1] = cubeT[1][1][0]
            cube[1][0][1] = cubeT[1][1][2]
            cube[1][2][2] = cubeT[1][2][0]
            cube[1][1][2] = cubeT[1][2][1]
            cube[1][0][2] = cubeT[1][2][2]

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

    if side == 3:
        if ccc == 'c':
            cube[2][0][0] = cubeT[1][2][0]  #Red from White
            cube[2][1][0] = cubeT[1][2][1]
            cube[2][2][0] = cubeT[1][2][2]

            cube[4][0][2] = cubeT[2][0][0]  #Yellow from Red
            cube[4][0][1] = cubeT[2][1][0]
            cube[4][0][0] = cubeT[2][2][0]

            cube[5][0][0] = cubeT[4][0][2]  #Orange from Yellow
            cube[5][1][0] = cubeT[4][0][1]
            cube[5][2][0] = cubeT[4][0][0]

            cube[1][2][0] = cubeT[5][0][0]  #White from Orange
            cube[1][2][1] = cubeT[5][1][0]
            cube[1][2][2] = cubeT[5][2][0]

            cube[3][0][0] = cubeT[3][2][0]  #Green from Green
            cube[3][0][1] = cubeT[3][1][0]
            cube[3][0][2] = cubeT[3][0][0]
            cube[3][1][0] = cubeT[3][2][1]
            cube[3][1][2] = cubeT[3][0][1]
            cube[3][2][0] = cubeT[3][2][2]
            cube[3][2][1] = cubeT[3][1][2]
            cube[3][2][2] = cubeT[3][0][2]

        if ccc == 'cc':
            cube[1][2][0] = cubeT[2][0][0]  #White from Red
            cube[1][2][1] = cubeT[2][1][0]
            cube[1][2][2] = cubeT[2][2][0]

            cube[2][0][0] = cubeT[4][0][2]  #Red from Yellow
            cube[2][1][0] = cubeT[4][0][1]
            cube[2][2][0] = cubeT[4][0][0]

            cube[4][0][2] = cubeT[5][0][0]  #Yellow from Orange
            cube[4][0][1] = cubeT[5][1][0]
            cube[4][0][0] = cubeT[5][2][0]

            cube[5][0][0] = cubeT[1][2][0]  #Orange from White
            cube[5][1][0] = cubeT[1][2][1]
            cube[5][2][0] = cubeT[1][2][2]

            cube[3][0][0] = cubeT[3][0][2]  #Green from Green
            cube[3][0][1] = cubeT[3][1][2]
            cube[3][0][2] = cubeT[3][2][2]
            cube[3][1][0] = cubeT[3][0][1]
            cube[3][1][2] = cubeT[3][2][1]
            cube[3][2][0] = cubeT[3][0][0]
            cube[3][2][1] = cubeT[3][1][0]
            cube[3][2][2] = cubeT[3][2][0]

    if side == 4:
        if ccc == 'c':
            cube[6][0][2] = cubeT[2][2][0]  #Blue from Red
            cube[6][0][1] = cubeT[2][2][1]
            cube[6][0][0] = cubeT[2][2][2]

            cube[2][2][0] = cubeT[3][2][0]  #Red from Green
            cube[2][2][1] = cubeT[3][2][1]
            cube[2][2][2] = cubeT[3][2][2]

            cube[3][2][2] = cubeT[5][0][0]  #Green from Orange
            cube[3][2][1] = cubeT[5][0][1]
            cube[3][2][0] = cubeT[5][0][2]

            cube[5][0][0] = cubeT[6][0][0]  #Orange from Blue
            cube[5][0][1] = cubeT[6][0][1]
            cube[5][0][2] = cubeT[6][0][2]

            cube[4][0][2] = cubeT[4][0][0]  #Yellow from Yellow
            cube[4][1][2] = cubeT[4][0][1]
            cube[4][2][2] = cubeT[4][0][2]
            cube[4][0][1] = cubeT[4][1][0]
            cube[4][1][1] = cubeT[4][1][1]
            cube[4][2][1] = cubeT[4][1][2]
            cube[4][0][0] = cubeT[4][2][0]
            cube[4][1][0] = cubeT[4][2][1]
            cube[4][2][0] = cubeT[4][2][2]

        if ccc == 'cc':
            cube[2][2][0] = cubeT[6][0][2]  #Red from Blue
            cube[2][2][1] = cubeT[6][0][1]
            cube[2][2][2] = cubeT[6][0][0]

            cube[3][2][0] = cubeT[2][2][0]  #Green from Red
            cube[3][2][1] = cubeT[2][2][1]
            cube[3][2][2] = cubeT[2][2][2]

            cube[5][0][0] = cubeT[3][2][2]  #Orange from Green
            cube[5][0][1] = cubeT[3][2][1]
            cube[5][0][2] = cubeT[3][2][0]

            cube[6][0][0] = cubeT[5][0][0]  #Blue from Orange
            cube[6][0][1] = cubeT[5][0][1]
            cube[6][0][2] = cubeT[5][0][2]

            cube[4][0][0] = cubeT[4][0][2]  #Yellow from Yellow
            cube[4][0][1] = cubeT[4][1][2]
            cube[4][0][2] = cubeT[4][2][2]
            cube[4][1][0] = cubeT[4][0][1]
            cube[4][1][1] = cubeT[4][1][1]
            cube[4][1][2] = cubeT[4][2][1]
            cube[4][2][0] = cubeT[4][0][0]
            cube[4][2][1] = cubeT[4][1][0]
            cube[4][2][2] = cubeT[4][2][0]











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