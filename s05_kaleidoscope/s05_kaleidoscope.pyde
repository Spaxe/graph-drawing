traces = []
start_size = 16

dist_threshold = 128
last_mouseX = 0
last_mouseY = 0

def setup():
    size(640, 640)
    background(0)
    colorMode(RGB, 1.0)
    ellipseMode(CENTER)
    
def mouseMoved():
    s = min(dist(last_mouseX, last_mouseY, mouseX, mouseY), start_size)
    if len(traces) < 100:
        traces.append([mouseX, mouseY, s])
        traces.append([width - mouseX, mouseY, s])
        traces.append([mouseX, height - mouseY, s])
        traces.append([width - mouseX, height - mouseY, s])
    last_mouseX, last_mouseY = mouseX, mouseY
    
def draw():
    background(0)

    for t in traces:
        c = sqrt(float(t[0]) / width)
#         fill(c, 0.1, 1-c)
#         stroke(0)
#         ellipse(t[0], t[1], t[2], t[2])
        t[2] /= 1.1
        
        noFill()
        stroke(c, 0.1, 1-c)
        poly = []
#         with beginShape():
        for r in traces:
            distance = dist(r[0], r[1], t[0], t[1]) 
            if 0 < distance <= dist_threshold:
                poly.append(r)
#                     curveVertex(r[0], r[1])
                    
        if len(poly) > 3:
            noStroke()
            fill(c, 0.1, 1-c, 0.1)
            with beginShape():
                for p in poly:
                    curveVertex(p[0], p[1])
        
        if t[2] < 1:
            traces.remove(t)
    
    
