# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 10:09:31 2022

@author: manoj
"""

points = [input().split() for _ in range(int(input()))]
for i, (x, y) in enumerate(points):
    if y == points[i+1][1]:
        start, end, alt = int(x), int(points[i+1][0]), int(y)
        mid = (start + end) / 2
        break

while 1:
    x, y, h_speed, v_speed, *_ = [int(i) for i in input().split()]
    power = 4
    rotate = -20 if x < mid else 20
    if v_speed > 0:
        power = 0
    if abs(h_speed) > 80:
        rotate *= -1
    if abs(x - mid) < 1300:
        if abs(h_speed) > 10:
            rotate = 60 if h_speed > 0 else -60
        else:
            rotate = 0
            if v_speed < -36:
                power = 4
            else:
                power = 0
        if y - alt < 90:
            rotate = 0

    print(rotate, power)
    
    _______________________________________________________________________________________
    
    import sys
from math import radians, degrees, cos, sin, acos, asin, hypot

surface_n = int(input())
land_x1, land_y1 = -1, -1
for i in range(surface_n):
    land_x2, land_y2 = [int(j) for j in input().split()]
    if land_x2 - land_x1 >= 1000 and land_y2 == land_y1:
        target_left, target_right = land_x1, land_x2
        target_y = land_y2
    land_x1, land_y1 = land_x2, land_y2

max_speed = 60
g = 3.711 # m/s**2

while True:
    x, y, h_speed, v_speed, fuel, rotate, power = [int(i) for i in input().split()]
    angle = radians(90 - rotate)
    
    # target_y = -(1 / 2) * g * t ** 2 + (-v_speed) * t + y
    # v(t) = -g * t + (-v_speed)
    
    # g_x = cos(angle) * p
    # g_y = sin(angle) * p - g
    
    # landing
    if x > target_left and x < target_right and abs(h_speed) < 5:
        sec_2_stop = v_speed / (4 - g)
        height_at_stop = (1 / 2) * (4 - g) * sec_2_stop ** 2 - v_speed * sec_2_stop + y
        p = 4 if height_at_stop <= target_y else 0
        r = 0
        
    # moving horizontally
    else:
        p = 4
        if x < target_left:
            v_x = max_speed
        elif x > target_right:
            v_x = -max_speed
        else:
            v_x = 0
        v_y = 0
        direction = -1 if h_speed > v_x else 1
        cos_a = (v_x - h_speed) / p
        sin_a = (v_y - v_speed + g) / p
        angle = asin(sin_a / hypot(cos_a, sin_a))
        r = direction * round(degrees(angle) - 90)
        if abs(r) == 180:
            p = 0
            r = 0
        else:
            r = max(-90, min(90, r))
            
    print(r, p)

    ___________________________________________________________________________
    
    import sys
import math

class MarsLander:
    def __init__(t,arr):
        t.x, t.y, t.dx, t.dy, t.fuel, t.angle, t.power, t.targetL, t.targetR, t.targetY=arr 
        t.Y_MARGIN = 20
        t.SPEED_MARGIN = 5
        t.MAX_DY = 40
        t.MAX_DX = 20
        t.GRAVITY = 3.711
    def isOverTarget(t):
        return t.targetL <=t. x and t.x <= t.targetR
    def isFinishing(t):
        return t.y < t.targetY + t.Y_MARGIN
    def hasSafeSpeed(t):
        return abs(t.dx) <= t.MAX_DX - t.SPEED_MARGIN and abs(t.dy) <= t.MAX_DY - t.SPEED_MARGIN
    def goesInWrongDirection(t):
        return (t.x < t.targetL and t.dx < 0) or (t.targetR < t.x and t.dx > 0)
    def goesTooFastHorizontally(t):
        return abs(t.dx) > 4*t.MAX_DX;
    def goesTooSlowHorizontally(t):
        return abs(t.dx) < 2*t.MAX_DX;
    def angleToSlow(t):
        speed = (t.dx**2 + t.dy**2)**0.5
        return int(math.degrees(math.asin(t.dx / speed)))
    def angleToAimTarget(t):
        angle = int(math.degrees(math.acos(t.GRAVITY / 4.0)))
        if (t.x < t.targetL):
            return -angle
        elif t.targetR < t.x:
            return angle
        else:
            return 0
    def powerToHover(t):
        if t.dy >= 0:return 3
        else:return 4
    
land=[]
for i in range(int(input())):
    land_x, land_y = [int(j) for j in input().split()]
    print(land_x, land_y, file=sys.stderr)
    land+=[(land_x, land_y)]

def getLandPoint():
    for i in range(1,len(land)):
        if land[i][1]==land[i-1][1]:
            return land[i-1][0],land[i][0],land[i-1][1]
    return -1,-1,-1    

tx1,tx2,ty=getLandPoint()

while True:

    ship = MarsLander([int(i) for i in input().split()]+[tx1,tx2,ty])
    
    if not(ship.isOverTarget()):
        if ship.goesInWrongDirection() or ship.goesTooFastHorizontally():
            print(ship.angleToSlow(), 4)
        elif ship.goesTooSlowHorizontally():
            print(ship.angleToAimTarget(), 4)
        else:
            print(0, ship.powerToHover())
    else:
        if ship.isFinishing():
            print(0, 3)
        elif ship.hasSafeSpeed():
            print(0, 2)
        else: 
            print(ship.angleToSlow(), 4)
    #print(x,y,h_speed,v_speed,tx1,tx2,ty, file=sys.stderr)

    _________________________________________________________________________
    
    import sys
import math


class Point:
    """ Point class represents and manipulates x,y coords. """

    def __init__(self, x=0, y=0):
        """ Create a new point at x, y """
        self.x = x
        self.y = y
        
    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)        
        

class PID:
  """Generic PID controller class

    This class allows to control an input/output relationship
    through a PID controller, tuned by 3 parameters Kp, Ki and Kd.
  """

  def __init__(self, Kp=0.2, Ki=0.0, Kd=0.0, cMin=0, cMax=1):

    self.Kp = Kp
    self.Ki = Ki
    self.Kd = Kd
    self.cMin = cMin
    self.cMax = cMax

    self.seekP = 0.0
    self.P = 0.0
    self.I = 0.0
    self.D = 0.0
    self.oldT = -1
    self.oldInput = 0.0

  def seek(self, seekVal, curVal, log):
    """Computes new input value based on current and expected output values"""

    P = seekVal - curVal
    D = self.D
    I = self.I
    newInput = self.oldInput

    if self.oldT >= 0:
      D = P - self.P
      onlyPD = self.Kp * P + self.Kd * D
    
      if ((self.I > 0 or onlyPD > self.cMin)
      and (self.I < 0 or onlyPD < self.cMax)):
        I = self.I + P
    
      newInput = onlyPD + self.Ki * I
    
    print("{} : {}".format(log, newInput), file=sys.stderr)
    newInput = max(self.cMin, min(self.cMax, newInput))

    self.seekP = seekVal
    self.P = P
    self.I = I
    self.D = D
    self.oldT = 0
    self.oldInput = newInput

    return newInput

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

landscape = []

surface_n = int(input())  # the number of points used to draw the surface of Mars.
for i in range(surface_n):
    # land_x: X coordinate of a surface point. (0 to 6999)
    # land_y: Y coordinate of a surface point. By linking all the points together in a sequential fashion, you form the surface of Mars.
    land_x, land_y = [int(j) for j in input().split()]
    landscape.append(Point(land_x, land_y))
    
#Determine the coordinates of the landing area
landing_area = []
found = False
i = 0
while not found and i < len(landscape)-1:
    if landscape[i].y == landscape[i+1].y and landscape[i+1].x - landscape[i].x >= 1000:
        landing_area.append(landscape[i])
        landing_area.append(landscape[i+1])
        break
    
    i +=1    
   
    
tgt_x = (landing_area[0].x + landing_area[1].x) / 2

pid_thr = PID(0.6, 0, 0.01, 1, 4)
pid_rot = PID(-0.05, 0, -1.2, -45, 45)

# game loop
while True:
    # h_speed: the horizontal speed (in m/s), can be negative.
    # v_speed: the vertical speed (in m/s), can be negative.
    # fuel: the quantity of remaining fuel in liters.
    # rotate: the rotation angle in degrees (-90 to 90).
    # power: the thrust power (0 to 4).
    x, y, h_speed, v_speed, fuel, rotate, power = [int(i) for i in input().split()]
        
    alt = y - landing_area[0].y    
    above_zone = x > landing_area[0].x and x < landing_area[-1].x
    horiz_slow = h_speed < 20 and h_speed > -20
    
    # if (alt < 600 and not above_zone): 
    #     if v_speed > 0:
    #         power = 3
    #     else:
    #         power = 4
            
    #     if x < tgt_x:
    #         rotate =  -15 
    #     else:
    #         rotate = 15
    # else:
    if (above_zone and horiz_slow):
        power = pid_thr.seek(-30, v_speed, 'thr')
    else:
        power = 4
    
    if (horiz_slow and alt < 150):
        rotate = 0
    else:
        rotate = pid_rot.seek(tgt_x, x, 'rot')
        
    if (alt < 600 and not above_zone):
        rotate =  max(-10, min(10, rotate))
    
    

    print("Alt: {}".format(alt), file=sys.stderr)
    print("Above zone: {}".format(above_zone), file=sys.stderr)
    
    # rotate power. rotate is the desired rotation angle. power is the desired thrust power.
    print("{} {}".format(int(rotate), int(power)))

    _______________________________________________________________________________________________________
    
    
   import sys
import math

surface_n = int(input())
surface = [[int(x) for x in input().split()] for i in range(surface_n)]
print(surface, file=sys.stderr)

for i in range(surface_n -1):
    if(surface[i][1] == surface[i+1][1]):
        landing_zone = ((surface[i][0], surface[i+1][0]), surface[i][1])
        #landing_zone = ((surface[i][0] + surface[i+1][0])//2, surface[i][1])
print(landing_zone, file=sys.stderr)

def distance_to_stop(h_speed):
    unit_speed = h_speed/(h_thrust_speed*3)
    return unit_speed*(unit_speed+1)/2+h_speed*2

# First part: move above platform
def move_above_platform():
    while(True):
        x, y, h_speed, v_speed, fuel, rotate, power = [int(i) for i in input().split()]
        if(x > landing_zone[0][1]):
            direction = "LEFT";
            x_distance = x -landing_zone[0][1];
            if(v_speed <-5):
                print(-h_thrust_angle//3, 4)
            else:
                print(-h_thrust_angle, 4)
        elif(x < landing_zone[0][0]):
            direction = "RIGHT"
            x_distance = x - landing_zone[0][0]
            if(v_speed <-5):
                print(h_thrust_angle//3, 4)
            else:
                print(h_thrust_angle, 4)
        #x_distance = x - landing_zone[0]
        print(h_speed, h_speed + h_thrust_speed, file=sys.stderr)
        if(abs(x_distance) < distance_to_stop(h_speed)): ##this is not correct
            break;

# Second part: break and stabilize        
def break_stabilize(): #function is not precise, often creates a loop
    #TODO fix stabilitzation. maybe put a larger angle in case there's not enough space to stop
    while(True):
        x, y, h_speed, v_speed, fuel, rotate, power = [int(i) for i in input().split()]
        if h_speed > 0:
            x_distance = x- landing_zone[0][1]
        else:
            x_distance = x -landing_zone[0][0]
        unit_speed = h_speed/(h_thrust_speed*4)
        
        if(abs(x_distance) < unit_speed*(unit_speed+1)/2):
            if(h_speed > 0):
                angle_to_stop = 90
            else:
                angle_to_stop = -90
        elif(abs(h_speed) < (h_thrust_speed*4)):
            angle_to_stop = math.ceil(math.degrees(math.acos(-h_speed)))//2 -90
        elif(h_speed > 0):
            angle_to_stop = -h_thrust_angle
        else:
            angle_to_stop = h_thrust_angle
        
        print(angle_to_stop, 4)
        if(abs(h_speed) < 1 * abs(rotate) < 15):
            break;

# Third part: free fall
def free_fall():
    while(True):
        x, y, h_speed, v_speed, fuel, rotate, power = [int(i) for i in input().split()]
        v_distance = y - landing_zone[1]
        unit_speed = (v_speed+15)/v_thrust_speed
        print(0,0)
        if(v_distance < unit_speed*(unit_speed+1)/2):
            break;


# Fourth part: land    
def land():
    while(True):
        print(0,4)
        
# Main Program
v_thrust_speed = 4-3.711
h_thrust_angle = math.ceil(math.degrees(math.asin(3.711/4))) - 92 #not sure about / TODO
h_thrust_speed = math.cos(math.radians(h_thrust_angle+90))
print(h_thrust_angle, h_thrust_speed, file=sys.stderr)

move_above_platform()
break_stabilize()
free_fall()
land()

________________________________________________________________________________________________

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

surface_n = int(input())  # the number of points used to draw the surface of Mars.
surface = []
for i in range(surface_n):
    # land_x: X coordinate of a surface point. (0 to 6999)
    # land_y: Y coordinate of a surface point. By linking all the points together in a sequential fashion, you form the surface of Mars.
    land_x, land_y = [int(j) for j in input().split()]
    surface.append([land_x, land_y])

destination_y = surface[0][1]
destination_x1, destination_x2 = surface[0][0], surface[-1][0]
for i in range(1, surface_n):
    x_prev, y_prev = surface[i - 1]
    x, y = surface[i]
    if y_prev == y:
        destination_y = y
        destination_x1 = x_prev
        destination_x2 = x
        break

# game loop
while True:
    # h_speed: the horizontal speed (in m/s), can be negative.
    # v_speed: the vertical speed (in m/s), can be negative.
    # fuel: the quantity of remaining fuel in liters.
    # rotate: the rotation angle in degrees (-90 to 90).
    # power: the thrust power (0 to 4).
    x, y, h_speed, v_speed, fuel, rotate, power = [int(i) for i in input().split()]

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    tgt_x = (destination_x1 + destination_x2) / 2
    width_x = destination_x2 - destination_x1
    distance = ((x - tgt_x)**2 + (y - destination_y)**2)**0.5

    angle = 0
    thurst = 2

    above_center = destination_x1 + width_x // 4 < x < destination_x2 - width_x // 4
    above = destination_x1 < x < destination_x2
    h_speed_limit = 10 if (not above and y < destination_y + 250) else (19 if above else (35 if abs(x - tgt_x) < 3500 else 44))
    v_speed_limit = 35 if above_center else 20

    print(f"destination {[tgt_x, destination_y]}, distance: {abs(x -tgt_x)} {abs(y - destination_y)} {distance} above {above} {above_center}", file=sys.stderr, flush=True)

    angle_mult = 35

    direction = -1 if x < tgt_x else 1
    if above_center:
        angle = 0
    else:
        if above and abs(y - destination_y) < 300:
            angle_mult = 0
        elif y < destination_y + 150:
            angle_mult = 4
            thurst = 4
        angle = direction * angle_mult

    if abs(h_speed) > h_speed_limit:
        sign = -1 if h_speed < 1 else 1
        angle = sign * min(abs(h_speed // 10) * angle_mult, angle_mult)
        thurst = 4

    if v_speed > v_speed_limit:
        thurst = 1
    elif abs(v_speed) > v_speed_limit:
        thurst = 4

    # rotate power. rotate is the desired rotation angle. power is the desired thrust power.
    print(f"{angle} {thurst}")

    __________________________________________________________________________________________________
    
    import sys
import math

def rota(x,h_speed,midX_landing,lenght):
    global tilt, tilt_, xx, xxx
    if tilt_ == 0: # one time variable whether starting from right or left of pad
        tilt = 1 if x > midX_landing else -1
        tilt_ +=1

    if abs(x- midX_landing)<length_landing:
        if abs(h_speed) < 15 and abs(x+((y-flay_y)/abs(v_speed))*h_speed-midX_landing)<0.375*length_landing: #if current vectors land rocket within pad rotate 0
            return 0
        else:
            xx -=0.025
            xxx = (max(0, xx))
            yy = int(math.atan((x-(midX_landing+length_landing*xxx*tilt))/100)*35) #move target x lineary towards mid pad and rotate arctan of difference
            return yy
    else:
        return int((h_speed+80*tilt)*0.5)  

def powa(flat_x1,flat_x2,flat_y,y):
    return 3 if abs(h_speed) < 15 and v_speed > -35 else 4 # if too slow thrust down    

xx = 1
land_x2 = []
land_y2 = []
flat_x1 = 0
flat_x2 = 0
flay_y = 0
surface_n = int(input())  # the number of points used to draw the surface of Mars.
tilt_ = 0
tilt = 0

for i in range(surface_n):
    land_x, land_y = [int(j) for j in input().split()]
    land_x2.append(land_x)
    land_y2.append(land_y)

for i2 in range(len(land_y2)-1):
    if land_y2[i2] == land_y2[i2+1]:
        flat_x1 = land_x2[i2]
        flat_x2 = land_x2[i2+1]
        flat_y = land_y2[i2]
    else:
        pass

midX_landing = (flat_x1+flat_x2)//2 # mid x of landing pad
length_landing = abs(flat_x2-flat_x1) # landing width

while True:
    x, y, h_speed, v_speed, fuel, rotate, power = [int(i) for i in input().split()]
    rot = rota(x,h_speed,midX_landing,length_landing)
    powaa = powa(flat_x1,flat_x2,flat_y,y)
    print(rot, powaa)

    ___________________________________________________________________________________________
    
    
    
    
