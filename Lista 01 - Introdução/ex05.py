import math
from math import sqrt

buraco = int(input())
xcoelho, ycoelho = map(float, input().split())
xraposa, yraposa = map(float, input().split())

for i in range(buraco):

    xburaco, yburaco = map(float, input().split())
    distCoelho = sqrt((((xcoelho - xburaco)**2) + ((ycoelho - yburaco))**2))
    distRaposa = (sqrt((((xraposa - xburaco)**2) + ((yraposa - yburaco))**2)))/2

    if distRaposa >= distCoelho:
        print(f'O coelho pode escapar pelo buraco ({xburaco:.3f}, {yburaco:.3f}).')
        break

else:
    print('O coelho nao pode escapar.')
