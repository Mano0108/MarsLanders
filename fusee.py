import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
points = [input().split() for _ in range(int(input()))]
for i, (x, y) in enumerate(points):
    if y == points[i+1][1]:
        start, end, alt = int(x), int(points[i+1][0]), int(y)
        mid = (start + end) / 2
        break




def EvalFunction(X, Y, H_SPEED, V_SPEED, ROTATE,X_TARGET, Y_TARGET):
    result = []
    
    if ROTATE == 0 and H_SPEED<=40.0 and V_SPEED <= 20.0 and Y==Y_TARGET: 
        result.append(1)
    else :
        result.append(0)
    
    result.append(math.sqrt((Y_TARGET-Y)**2+(X_TARGET-X)**2))

    return result

    
# game loop
while True:
    
    # h_speed: the horizontal speed (in m/s), can be negative.
    # v_speed: the vertical speed (in m/s), can be negative.
    # fuel: the quantity of remaining fuel in liters.
    # rotate: the rotation angle in degrees (-90 to 90).
    # power: the thrust power (0 to 4).
    x, y, h_speed, v_speed, fuel, rotate, power = [int(i) for i in input().split()]

    print(EvalFunction(x,y,h_speed,v_speed,rotate,mid,alt))
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    # rotate power. rotate is the desired rotation angle. power is the desired thrust power.
    print("-20 3")



