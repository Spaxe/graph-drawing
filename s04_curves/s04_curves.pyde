traces = []
start_size = 16

dist_threshold = 256
last_mouseX = 0
last_mouseY = 0

def setup():
    size(800, 800)
    background(0)
    colorMode(RGB, 1.0)
    ellipseMode(CENTER)
    
def mouseMoved():
    s = min(dist(last_mouseX, last_mouseY, mouseX, mouseY), start_size)
    if len(traces) < 100:
        traces.append([mouseX, mouseY, s])
    last_mouseX, last_mouseY = mouseX, mouseY
    
def draw():
    background(0)

    for t in traces:
        c = float(t[1]) / height
        fill(c, 0.1, 1-c)
        stroke(0)
        ellipse(t[0], t[1], t[2], t[2])
        t[2] /= 1.1
        
        noFill()
        stroke(c, 0.1, 1-c)
        beginShape()
        for r in traces:
            distance = dist(r[0], r[1], t[0], t[1]) 
            if 0 < distance <= dist_threshold:
                curveVertex(r[0], r[1])
        endShape()
        
        if t[2] < 1:
            traces.remove(t)
    
    
