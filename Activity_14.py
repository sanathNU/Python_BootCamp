import math


def inputval():
    print("Enter the values of length,breadth and height in same order respectively: \n")
    l,b,h = map(int,input().split())
    return l,b,h

def volTromb(l,b,h):
    #The forumula is Vol = (b^2 * h^2)/(sqrt(l^2+b^2+h^2))
    vol = (b**2 * h**2)/pow( l**2 + b**2 + h**2,1/2)
    return vol

def Radii(volume):
    #The Formula is cuberoot( Volume*3/(4*pi) )
    radius = pow((volume*3)/(4*math.pi),1/3)
    return radius

def display(volume,radius):
    print('The volume of the tromboloid is %.3f' %volume)
    print('The radiss of sphere with same volume is %.3f' %radius)
    
def main():
    #assigning values
    l,b,h = inputval()
    #volume of tromboid
    vol = volTromb(l,b,h)
    #radii of sphere
    radius = Radii(vol)
    display(vol,radius)
    
main()
