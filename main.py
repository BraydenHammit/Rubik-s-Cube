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
            cubeT[1][0][2] = cube[3][0][2]  #top right white side should be from top right green side