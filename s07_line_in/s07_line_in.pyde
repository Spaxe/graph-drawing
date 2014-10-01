add_library('minim')

traces = []
start_size = 32
buffer_size = 256

dist_threshold = 32
last_mouseX = 0
last_mouseY = 0

def setup():
    size(1024, 640)
    background(0)
    colorMode(RGB, 1.0)
    ellipseMode(CENTER)

    global minim
    minim = Minim(this)
    global line_in
    line_in = minim.getLineIn(minim.STEREO, buffer_size)
    
    for i in range(buffer_size):
        traces.append([i*4, height/2, start_size])

def draw():
    background(0)
    
    for i in xrange(line_in.bufferSize()):
        traces[i] = [i*4, 
                     (traces[i][1] + line_in.left.get(i)*height) / 2 + height/4, 
                     start_size]

    for t in traces:
        c = sqrt(float(t[0]) / width)
        
        noFill()
        stroke(1-c, 0.1, 1-c)
        poly = []
        for r in traces:
            distance = dist(r[0], r[1], t[0], t[1]) 
            if 0 < distance <= dist_threshold:
                poly.append(r)
                    
        if len(poly) > 3:
            noStroke()
            fill(abs(sin(float(frameCount)/120)), c, 1-c, 0.4)
            with beginShape():
                for p in poly:
                    curveVertex(p[0], p[1])
    
def stop():
    line_in.close()
    minim.stop()
