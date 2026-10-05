cube = {
    1: [['W','W','W'],['W','W','W'],['W','W','W']],    
    2: [['R','R','R'],['R','R','R'],['R','R','R']],
    3: [['G','G','G'],['G','G','G'],['G','G','G']],   
    4: [['Y','Y','Y'],['Y','Y','Y'],['Y','Y','Y']],
    5: [['O','O','O'],['O','O','O'],['O','O','O']],
    6: [['B','B','B'],['B','B','B'],['B','B','B']]
}

FACE_FRAMES = {
    1: ((0, 1, 0), (1, 0, 0), (0, 0, -1)),  # Up
    2: ((0, 0, 1), (1, 0, 0), (0, 1, 0)),   # Front
    3: ((1, 0, 0), (0, 0, -1), (0, 1, 0)),  # Right
    4: ((0, -1, 0), (1, 0, 0), (0, 0, 1)),  # Down
    5: ((-1, 0, 0), (0, 0, 1), (0, 1, 0)),  # Left
    6: ((0, 0, -1), (-1, 0, 0), (0, 1, 0)), # Back
}
NORMAL_TO_FACE = {frame[0]: face for face, frame in FACE_FRAMES.items()}


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def cross(a, b):
    return (
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0],
    )


def rotate_vector(vector, axis, turns):
    for _ in range(turns % 4):
        parallel = tuple(dot(vector, axis) * component for component in axis)
        perpendicular = cross(axis, vector)
        vector = tuple(parallel[i] - perpendicular[i] for i in range(3))
    return vector


def sticker_position(face, row, column):
    normal, right, up = FACE_FRAMES[face]
    return tuple(
        normal[i] + (column - 1) * right[i] + (1 - row) * up[i]
        for i in range(3)
    )


def rotate(face, turns=1):
    """Turn face clockwise by `turns`; -1 is counterclockwise, 2 is a half-turn."""
    global cube
    if face not in FACE_FRAMES:
        raise ValueError("face must be between 1 and 6")
    if turns in ("c", "cw"):
        turns = 1
    elif turns in ("a", "ccw"):
        turns = -1
    if not isinstance(turns, int):
        raise ValueError("turns must be an integer or a direction string")

    turns %= 4
    if turns == 0:
        return

    axis = FACE_FRAMES[face][0]
    old = {number: [row[:] for row in grid] for number, grid in cube.items()}
    new_cube = {number: [row[:] for row in grid] for number, grid in old.items()}

    for source_face, grid in old.items():
        sticker_normal = FACE_FRAMES[source_face][0]
        for row in range(3):
            for column in range(3):
                position = sticker_position(source_face, row, column)
                normal = sticker_normal

                if dot(position, axis) == 1:
                    position = rotate_vector(position, axis, turns)
                    normal = rotate_vector(normal, axis, turns)

                target_face = NORMAL_TO_FACE[normal]
                target_normal, right, up = FACE_FRAMES[target_face]
                offset = tuple(position[i] - target_normal[i] for i in range(3))
                target_column = dot(offset, right) + 1
                target_row = 1 - dot(offset, up)
                new_cube[target_face][target_row][target_column] = grid[row][column]

    cube = new_cube