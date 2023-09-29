from pico2d import *
import random

WIDTH, HEIGHT = 1280, 1024
open_canvas(WIDTH, HEIGHT)
Hand = load_image("hand_arrow.png")
Character = load_image("run_animation.png")
Background = load_image("TUK_GROUND.png")
def Handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False


running = True
while running:
    Background.draw(WIDTH // 2, HEIGHT // 2)
    Draw_hand(x, y)
    update_canvas()
    Handle_events()

close_canvas()