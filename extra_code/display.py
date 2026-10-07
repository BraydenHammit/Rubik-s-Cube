def rectangles(can):
    can.configure(width=320, height=250)
    shapes = {1: [], 2: [], 3: []}
    faces = {
        1: ((160, 30), (30, 15), (-30, 15)),
        2: ((70, 75), (30, 15), (0, 30)),
        3: ((160, 120), (30, -15), (0, 30)),
    }

    for face, (o, h, v) in faces.items():
        for r in range(3):
            for c in range(3):
                x = o[0] + c * h[0] + r * v[0]
                y = o[1] + c * h[1] + r * v[1]
                points = (x, y, x + h[0], y + h[1], x + h[0] + v[0], y + h[1] + v[1], x + v[0], y + v[1],)
                id = can.create_polygon(*points, fill="white", outline="black")
                shapes[face].append(id)

    return shapes