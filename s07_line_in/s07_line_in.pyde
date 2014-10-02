add_library('minim')

traces = []
buffer_size = 256
mode = 0

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
        traces.append([i*4, height/2])

def draw():
    background(0)
    n = line_in.bufferSize()
    translate(width/2, height/2)
    
    if mode == 0:
        for i in xrange(n):
            traces[i] = [(traces[i][0] +
                         i*4-width/2) / 2, 
                        (traces[i][1] +
                         line_in.left.get(i)*height) / 2]
            
    elif mode == 1:
        for i in xrange(n):
            traces[i] = [(traces[i][0] +
                         cos(float(i)/n * 2 * PI) * height/4 + line_in.left.get(i) * height/2) / 2, 
                         (traces[i][1] + 
                         sin(float(i)/n * 2 * PI) * height/4 + line_in.right.get(i) * height/2) / 2]
            
    elif mode == 2:
        for i in xrange(n):
            traces[i] = [(traces[i][0] +
                         cos(float(i)/n * 2 * PI) * height/4 + line_in.left.get(i) * height) / 2, 
                         (traces[i][1] + 
                         sin(float(i)/n * 2 * PI) * height/4 + abs(line_in.right.get(i) * height/4) + abs((noise(i)-0.5) * height/2)) / 2]
            
    else:
        for i in xrange(n):
            traces[i] = [(traces[i][0] +
                         (cos(float(i)/n * 2 * PI) - 2.5 * cos(float(i)/n * 2 * PI)**((mode*2-1)**2)) * height/4 + line_in.left.get(i) * height/2) / 2, 
                         (traces[i][1] + 
                         (sin(float(i)/n * 2 * PI) - 2 * sin(float(i)/n * 2 * PI)**((mode*2-1)**2)) * height/4 + line_in.right.get(i) * height/2) / 2]

    for t in traces:
        c = 1
        if mode == 0:
            c = sqrt(float(abs(t[0])) / width)
        else:
            c = float(abs(t[1])) * 2 / height
        
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
    
def keyPressed():
    if key != CODED and key.isdigit() and key != '0':
        mode = max(int(key) - 1, 0)
    
def stop():
    line_in.close()
    minim.stop()
