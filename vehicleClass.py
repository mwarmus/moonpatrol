

def triangleMountain(w,h, perc=15):
    points = [[], []]
    proc = perc / 100
    lb = (0, 0)
    ct = (w/2, h)
    rb = (w, 0)
    points[0].append(lb)
    points[0].append(ct)
    points[0].append(rb)
    slb = (w/2 - (w/2 * h * proc) / h, h - h * proc)
    sct = (w/2, h)
    srb = (w/2 + (w/2 * h * proc) / h, h - h * proc)
    points[1].append(slb)
    points[1].append(sct)
    points[1].append(srb)
    return points




triangleMountain(300,200)