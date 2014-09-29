import sys

traces = []
logo = loadImage('python-logo.png')
start_size = 16

dist_threshold = 128
last_mouseX = 0
last_mouseY = 0

def setup():
    size(800, 800)
    background(0)
    colorMode(HSB, 1.0)
    ellipseMode(CENTER)
    
    print('Processing Python runs ' + sys.version)
    
def mouseMoved():
    s = min(dist(last_mouseX, last_mouseY, mouseX, mouseY), start_size)
    if len(traces) < 100:
        traces.append([mouseX, mouseY, s])
    last_mouseX, last_mouseY = mouseX, mouseY
    
def draw():
    background(0)

    for t in traces:
        fill(1, 0, 1, t[2]/start_size + 0.25)
        stroke(0)
        ellipse(t[0], t[1], t[2], t[2])
        t[2] /= 1.1
        
        for r in traces:
            distance = dist(r[0], r[1], t[0], t[1]) 
            if 0 < distance <= dist_threshold:
                stroke(1, 0, distance/dist_threshold)
                line(r[0], r[1], t[0], t[1])
        
        if t[2] < 1:
            traces.remove(t)
    
    
