from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 10
y = 90
while(1):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x, y)

    if x < 790 and y <= 90:
        x = x + 5
    elif x >= 790 and y < 580:
         y = y + 5
    elif x > 10 and y >= 580:
        x = x - 5
    elif x <= 10 and y > 90:
        y = y - 5

    delay(0.01)
    
close_canvas()
