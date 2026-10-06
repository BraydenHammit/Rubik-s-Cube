cube = {
    1: [['W','W','W'],['W','W','W'],['W','W','W']],    
    2: [['R','R','R'],['R','R','R'],['R','R','R']],
    3: [['G','G','G'],['G','G','G'],['G','G','G']],   
    4: [['Y','Y','Y'],['Y','Y','Y'],['Y','Y','Y']],
    5: [['O','O','O'],['O','O','O'],['O','O','O']],
    6: [['B','B','B'],['B','B','B'],['B','B','B']]
}

def rotate(side,ccc):
    global cube
    cubeT = cube.copy()
    if side == 1:
        if ccc == 'c':
            cube[1][0][2] = cubeT[3][0][2]  #White from Green
            cube[1][1][2] = cubeT[3][1][2]
            cube[1][2][2] = cubeT[3][2][2]
            cube[3][0][2] = cubeT[4][0][2]  #Green from Yellow
            cube[3][1][2] = cubeT[4][1][2]
            cube[3][2][2] = cubeT[4][2][2]
            cube[4][0][2] = cubeT[5][0][2]  #Yellow from Orange
            cube[4][1][2] = cubeT[5][1][2]
            cube[4][2][2] = cubeT[5][2][2]
            cube[5][0][2] = cubeT[1][0][2]  #Orange from White
            cube[5][1][2] = cubeT[1][1][2]
            cube[5][2][2] = cubeT[1][2][2]
            cube[2][0][0] = cubeT[2][2][0]  #Red from Red
            cube[2] = [list(row) for row in zip(*cubeT[2][::-1])]