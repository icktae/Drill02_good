from pico2d import *
import math

open_canvas()

# 오브젝트 생성
grass = load_image('grass.png')
character = load_image('character.png')

def run_circle() :
    print('CIRCLE')
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(400,90)
    delay(1)

    cx = 400
    cy = 300
    r = 200

    
    pass

def run_square() :
    print('SQUARE')
    pass

while True :
    run_circle()
    run_square()
    break
