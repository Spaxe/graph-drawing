dist_threshold = 64
start_size = 5
data = []
    
def setup():
    size(650, 650)
    background(0)
    colorMode(HSB, 1.0)
    strokeWeight(1)
    ellipseMode(CENTER)
    
    for i in range(150):
        data.append(sample(data))

def draw():
    for p in data:
        fill(p[0]/width / 5, 0.5, 1)
        noStroke()
        ellipse(p[0], p[1], start_size, start_size) 
        
def sample(points):
    if len(points) == 0:
        return [random(0, width), random(0, height)]
    
    max_dist, s = 0, None
    for i in range(10):
        p = [random(0, width), random(0, height)]
        c, distance = closest(points, p)
        if distance >= max_dist:
            max_dist, s = distance, p
    return s
            
def closest(points, x):
    min_dist = width * height
    result = None, None
    for p in points:
        distance = dist(x[0], x[1], p[0], p[1])
        if 0 < distance <= min_dist:
            result = p, distance
            min_dist = distance
    return result
           
def mouseMoved():
    for p in data:
        if dist(mouseX, mouseY, p[0], p[1]) <= dist_threshold:
            fill(p[0]/width / 5, 0.5, 1)
            stroke(p[0]/width / 5, 0.5, 1)
            line(mouseX, mouseY, p[0], p[1])
    
