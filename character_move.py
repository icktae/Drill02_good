from pico2d import *
import math

open_canvas()

# 오브젝트 생성
grass = load_image('grass.png')
character = load_image('character.png')

def run_circle() :
    print('CIRCLE')

    cx = 400
    cy = 300
    r = 200

    for deg in range(0, 360, 5) :
        x = cx + r * math.cos(deg / 360 * 2 * math.pi)
        y = cy + r * math.sin(deg / 360 * 2 * math.pi)
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        delay(0.01)

def run_square() :
    print('SQUARE')

    # bottom
    for x in range(50, 750, 10) :
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,90)
        delay(0.01)

    # up
    for y in range(90, 550, 10) :
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(750,y)
        delay(0.01)

        
    pass

while True :
   # run_circle()
    run_square()
    break
