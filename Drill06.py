from pico2d import *
import random

WIDTH, HEIGHT = 1280, 1024
open_canvas(WIDTH, HEIGHT)
Hand = load_image("hand_arrow.png")
Character = load_image("run_animation.png")
Background = load_image("TUK_GROUND.png")
running = True
mx, my = 0, 0
Point_x = []
Point_y = []


def Handle_events():
    global running, mx, my, Point_x, Point_y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            mx, my = event.x, HEIGHT - 1 - event.y
        elif event.type == SDL_MOUSEBUTTONDOWN:
            if event.button == SDL_BUTTON_LEFT:
                Point_x.append(mx)
                Point_y.append(my)
def Draw_hand(x, y):
    Hand.draw(x, y)
    for i in range(0, len(Point_x)):
        Hand.draw(Point_x[i], Point_y[i])
def Draw_Character():
    pass

while running:
    Background.draw(WIDTH // 2, HEIGHT // 2)
    Draw_hand(mx, my)
    Draw_Character()
    update_canvas()
    Handle_events()
    hide_cursor()

close_canvas()