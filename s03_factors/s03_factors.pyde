import math

dist_threshold = 64
start_size = 25
radius = 300
numbers = 16
numbers_limit = 256

data = lambda x: (cos(float(x)/numbers*math.pi*2)*radius, sin(float(x)/numbers*math.pi*2)*radius)
    
def setup():
    size(660, 660)
    colorMode(HSB, 1.0)
    textSize(16)
    textAlign(CENTER, CENTER)
    ellipseMode(CENTER)

def draw():
#     
#     driver = sin(float(frameCount*15)/width) * width
#     numbers = int(driver / width * numbers_limit)
#     start_size = max((1 - driver / width) * 29, 3)
#     
    translate(radius+25, radius+25)
    background(0)
    
    for x in range(2, numbers+1):
        p = data(x)
        for f in factors(x):
            if f == 1:
                continue
            q = data(f)
            strokeWeight(1)
            stroke(0, 0, 1, 0.25)
            line(p[0], p[1], q[0], q[1])

#     for x in range(2, numbers+1):
#         p = data(x)
#         
#         if len(factors(x)) > 2:
#             fill(float(x) / numbers / 5, 0.75, 1)
#         else:
#             fill(float(x) / numbers / 5, 0.5, 0.5)
#         stroke(0, 0, 1, 0.25)
#         strokeWeight(1)
#         ellipse(p[0], p[1], start_size, start_size) 
#         fill(0, 0, 0)
#         text(x, p[0], p[1])

def mouseMoved():
    numbers = int(float(mouseX) / width * numbers_limit)
    start_size = max((1 - float(mouseX) / width) * 29, 3)

def factors(n):    
    if n in range(2):
        return set()
    return set(reduce(list.__add__, 
                  ([i, n//i] for i in range(1, int(math.sqrt(n)) + 1) if n % i == 0)))
