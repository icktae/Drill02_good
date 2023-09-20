from pico2d import *
import math

open_canvas()

# 오브젝트 생성
grass = load_image('grass.png')
character = load_image('character.png')

# 화면출력 함수
def render_all(x, y):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        delay(0.1)

# 원 운동 함수
def run_circle() :
    print('CIRCLE')

    cx = 400
    cy = 300
    r = 200

    for deg in range(0, 360, 4) :
        clear_canvas_now()
        x = cx + r * math.cos(deg / 360 * 2 * math.pi)
        y = cy + r * math.sin(deg / 360 * 2 * math.pi)
        render_all(x, y)
        

# 사각 운동 함수       
def run_square() :
    print('SQUARE')

    # bottom
    for x in range(50, 750+1, 10) :
        render_all(x,90)

    # up
    for y in range(90, 550+1, 10) :
        render_all(750,y)

    # top
    for x in range(750, 50-1, -10) :
        render_all(x,550)

    # down
    for y in range(550, 90-1, -10) :
        render_all(50, y)

        
    pass

# 무한 루프
while True :
    run_circle()
    run_square()
