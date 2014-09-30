import math
import string

dist_threshold = 64
start_size = 25
radius = 500
numbers = 26
word = ""

data = lambda x: (cos(float(x)/numbers*math.pi*2)*radius, sin(float(x)/numbers*math.pi*2)*radius)
    
def setup():
    radius = min(650, 650) / 3
    size(650, 650)
    colorMode(HSB, 1.0)
    textAlign(CENTER)
    ellipseMode(CENTER)

def draw():
    with pushMatrix():
        translate(width / 2, height / 2)
        background(0)
        
        noFill()
        strokeWeight(1)
        stroke(0, 0, 1, 0.5)
        with beginShape():
            curveVertex(0, 0)
            curveVertex(0, 0)
            curveVertex(0, 0)
            for letter in word:
                value = 0
                if letter.upper() not in string.ascii_uppercase:
#                     curveVertex(0, 0)
                    continue
                else:
                    value = ord(letter.upper()) - 65
                p = data(value)
                
                curveVertex(p[0], p[1])
                
    fill(0, 0, 1)
    text(word, width /2, height /2)
            
def keyPressed():
    if key != CODED:
        if key == BACKSPACE:
            word = word[:-1]
        elif key == TAB:
            word = ""
        else:
            word += key
        
    
