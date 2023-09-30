from pico2d import *
WIDTH, HEIGHT = 1280, 1024
open_canvas(WIDTH, HEIGHT)
Hand = load_image("hand_arrow.png")
Character = load_image("run_animation.png")
Background = load_image("TUK_GROUND.png")
running = True
x1, y1, x2, y2 = WIDTH // 2, HEIGHT // 2, WIDTH // 2, HEIGHT // 2
start = [(x1, y1)]
end = [(x2, y2)]
mx, my = 0, 0
num = 0
frame = 0
arrive = 0
def handle_events():
    global running, mx, my, num, arrive
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            mx, my = event.x, HEIGHT - 1 - event.y
        elif event.type == SDL_MOUSEBUTTONDOWN:
            if event.button == SDL_BUTTON_LEFT:
                mx, my = event.x, HEIGHT - 1 - event.y
                end.append((mx, my))
            elif event.button == SDL_BUTTON_RIGHT:
                arrive += 1
# 주인공은 start[num]지점에서 end[num+1]까지 이동
# 주인공이 start지점에서 end지점까지 도달하면 start[num] = end[num+1]
# start.append(end[num])
# 주인공이 start 점에서 end 지점까지 도달하면 arrive += 1
def draw_hand(x, y):
    global arrive
    Hand.draw(x, y)
    for i in range(arrive+1, len(end)):
        Hand.draw(end[i][0], end[i][1])
def draw_character(x, y):
    global frame
    Character.clip_draw(frame * 100, 0, 100, 100, x, y)
    frame = (frame + 1) % 8

while running:
    clear_canvas()
    if len(end) > len(start):
        for i in range(0, 100 + 1, 3):
            Background.draw(WIDTH // 2, HEIGHT // 2)
            draw_hand(mx, my)
            t = i / 100
            x = (1 - t) * start[num][0] + t * end[num+1][0]
            y = (1 - t) * start[num][1] + t * end[num+1][1]
            draw_character(x, y)
            update_canvas()
            handle_events()
            delay(0.05)
        num += 1
        arrive += 1
        start.append((end[num][0], end[num][1]))
    else:
        Background.draw(WIDTH // 2, HEIGHT // 2)
        draw_hand(mx, my)
        draw_character(start[num][0], start[num][1])
        update_canvas()
        handle_events()
        delay(0.05)
    hide_cursor()

close_canvas()