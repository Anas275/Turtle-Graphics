import turtle
import colorsys
def modmuster():
    counter = 0
    nZacken = 7
    winke1 = 180 - (((nZacken-2) * 180 ) / nZacken )*2
    for y in range (40):

        for x in range (nZacken):
            c = colorsys.hsv_to_rgb(counter / 220, 1, 0.8)
            turtle.color('red')
            turtle.forward(200)
            turtle.left(180 - winke1)
            counter = counter + 1
        turtle.circle(100, -10)