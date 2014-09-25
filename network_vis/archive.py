# import math
# from itertools import permutations
# 
# names = ["ale", "beer", "cider"]
# data = zip(names, range(len(names)))
# angle = 2 * math.pi / len(data)
# radius = 100
# point_size = 10
# 
# def setup():
#     size(360, 360, P3D)
#     ellipseMode(CENTER)
#     colorMode(HSB, 100)
#     stroke(0, 0, 100)
#     strokeWeight(1)
#     fill(100)
# 
# def draw():
#     background(60, 60, 20)
#     translate(180, 180)
#     d_angle = frameCount / 100.0
#     
#     for datum, i in data:
#         ellipse(radius * cos(angle*i + d_angle), 
#                 radius * sin(angle*i + d_angle), 
#                 point_size, 
#                 point_size)
#     
#     for a, b in permutations(data, 2):
#         ax = radius * cos(angle*a[1] + d_angle)
#         ay = radius * sin(angle*a[1] + d_angle)
#         bx = radius * cos(angle*b[1] + d_angle)
#         by = radius * sin(angle*b[1] + d_angle)
#         line(ax, ay, bx, by)
