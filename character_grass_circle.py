from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

origin_x = 400
origin_y = 290
x = 400
y = 90
seta = 0
while(1):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x, y)

    x = origin_x + (200 * math.sin (seta / 360 * 2 * math.pi))
    y = origin_y + (200 * math.cos(seta / 360 * 2 * math.pi))
    seta = (seta + 30) % 360
    
    delay(0.05)
    
close_canvas()
