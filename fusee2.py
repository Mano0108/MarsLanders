import sys
import math
import random 
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
points = [input().split() for _ in range(int(input()))]

##trouver la plateforme 
for i, (x, y) in enumerate(points):
    if y == points[i+1][1]:
        start, end, alt = int(x), int(points[i+1][0]), int(y)
        mid = (start + end) / 2
        break

population = []

##definition de la zone d'atterissage 
def LandingZone(X,Y):
    if abs(X-mid)<1300 :
        return True
    else: 
        return False

##générer un gêne 
def GenGene(X,Y,H_SPEED,V_SPEED,MID,ALT):
    tabr = [i for i in range (0,40,10)]
    tabp = [i for i in range (3,5)]
    r = random.choice(tabr) if X > MID else - random.choice(tabr) 
    #r= -20 if X < mid else 20
    p = random.choice(tabp)
    #p=4
    if abs(H_SPEED)>80 and not LandingZone(X,Y):
        r*=-1
        return str(r) + " " + str(p)


    if LandingZone(X,Y):

        if abs(H_SPEED) > 10 :
            r = 60 if H_SPEED > 0 else -60
            p = 4
            if Y - ALT < 90:
                    r=0
            return str(r) + " " +str(p) 

        else:
            r = 0
            if V_SPEED < -36:
                p = 4
                return str(r) + " " +str(p)

            else:
                p = 0
                return str(r) + " " +str(p)


    return  str(r) + " " +str(p)


    

def EvalFunction(X, Y, H_SPEED, V_SPEED, ROTATE,X_TARGET, Y_TARGET):
    result = []
    if ROTATE == 0 and H_SPEED<=40.0 and V_SPEED <= 20.0 and Y==Y_TARGET: 
        result.append(1)
    else :
        result.append(0)
    result.append(math.sqrt((Y_TARGET-Y)**2+(X_TARGET-X)**2))
    return result


Chromosome = []
Distances = []
# game loop
while True:
    
    # h_speed: the horizontal speed (in m/s), can be negative.
    # v_speed: the vertical speed (in m/s), can be negative.
    # fuel: the quantity of remaining fuel in liters.
    # rotate: the rotation angle in degrees (-90 to 90).
    # power: the thrust power (0 to 4).
    x, y, h_speed, v_speed, fuel, rotate, power = [int(i) for i in input().split()]
    
    #Chromosome = [GenGene(x,y,h_speed,v_speed,mid,alt) for i in range (10)]
    #for i in Chromosome: 
    a = GenGene(x,y,h_speed,v_speed,mid,alt)
    Chromosome.append(a)
    Distances.append(EvalFunction(x,y,h_speed,v_speed,rotate,mid,alt))

    print(a)


    #print(GenGene(x,y,h_speed,v_speed,mid,alt))
    #print(EvalFunction(x,y,h_speed,v_speed,rotate,mid,alt))


    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    # rotate power. rotate is the desired rotation angle. power is the desired thrust power.
    #print("-20 3")


