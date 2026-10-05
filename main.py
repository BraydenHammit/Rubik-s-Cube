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
    if side == 2:
        if ccc == 'c':
            old = {face: [row[:] for row in stickers] for face, stickers in cube.items()}
            ring = [1, 3, 4, 5]
            for index, target in enumerate(ring):
                source = ring[(index + 1) % len(ring)]
                for row in range(3):
                    cube[target][row][2] = old[source][row][2]
            cube[2] = [list(row) for row in zip(*old[2][::-1])]