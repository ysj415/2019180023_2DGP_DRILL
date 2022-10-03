from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024

def change_frame_y(event):
    global frame_y

    if event.type == SDL_KEYDOWN:
        if frame_y == 2:
            frame_y = 0
        elif frame_y == 3:
            frame_y = 1
    elif event.type == SDL_KEYUP:
        if frame_y == 0:
            frame_y = 2
        elif frame_y == 1:
            frame_y = 3

def handle_events():
    global running
    global dir_x,dir_y
    global frame_x, frame_y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_LEFT:
                frame_y = 0
                dir_x -= 1
            elif event.key == SDLK_RIGHT:
                frame_y = 1
                dir_x += 1
            elif event.key == SDLK_UP:
                change_frame_y(event)
                dir_y += 1
            elif event.key == SDLK_DOWN:
                change_frame_y(event)
                dir_y -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_LEFT:
                frame_y = 2
                dir_x += 1
            elif event.key == SDLK_RIGHT:
                frame_y = 3
                dir_x -= 1
            elif event.key == SDLK_UP:
                change_frame_y(event)
                dir_y -= 1
            elif event.key == SDLK_DOWN:
                change_frame_y(event)
                dir_y += 1


open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
dir_x, dir_y = 0,0
frame_x, frame_y = 0, 3

while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    character.clip_draw(frame_x * 100, frame_y * 100, 100, 100, x, y)
    update_canvas()
    handle_events()

    frame_x = (frame_x + 1) % 8

    x += dir_x * 10
    y += dir_y * 10
    delay(0.05)
close_canvas()




