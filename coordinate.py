def on_line(p1, p2, x1):
    m = (p2[1]-p1[1])/(p2[0]-p1[0])
    y2 = p1[1]
    x2 = p1[0]
    y1 = m * (x1-x2)+y2
    return y1
