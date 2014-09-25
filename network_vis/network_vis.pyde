def setup():
    size(360, 360, P3D)
    ellipseMode(CENTER)
    colorMode(HSB, 100)
    stroke(0, 0, 100)
    strokeWeight(1)
    fill(100)
    
    for i in range(10):
        prin(i, numbers[i]);
    
def draw():
    background(0)
    
