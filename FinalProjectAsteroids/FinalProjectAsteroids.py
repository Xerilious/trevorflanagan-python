WIDTH = 800
HEIGHT = 600

center = WIDTH / 2, HEIGHT / 2
circle_image = 'circle'
left_arrow_image = 'left-arrow'
right_arrow_image = 'right-arrow'
current_actor = Actor(circle_image)
current_actor.pos = center

def draw():
    screen.fill((128, 0, 0))
    current_actor.draw()

def update():

    if keyboard.left:
        current_actor.image = left_arrow_image
    elif keyboard.right:
        current_actor.image = right_arrow_image
    else:
        current_actor.image = circle_image
