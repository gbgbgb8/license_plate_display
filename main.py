import time
import random
from galactic import GalacticUnicorn
from picographics import PicoGraphics, DISPLAY_GALACTIC_UNICORN as DISPLAY

gu = GalacticUnicorn()
graphics = PicoGraphics(DISPLAY)

width = GalacticUnicorn.WIDTH
height = GalacticUnicorn.HEIGHT

# Text settings
texts = ["3 SAM 123", "Uber Lyft", "3 SAM 123", "Lyft Uber"]
text_durations = [4, 1, 4, 1]  # Durations in seconds for each text
text_color = graphics.create_pen(255, 255, 255)  # Initial white text

# Set larger font
graphics.set_font("bitmap8")

# Blinking background settings
color = (255, 0, 0)  # Initial red background
lifetime = [[0.0 for y in range(height)] for x in range(width)]
age = [[0.0 for y in range(height)] for x in range(width)]

current_text_index = 0
text_start_time = time.ticks_ms()

# Themed color schemes
themed_color_schemes = {
    "Spring": [((0, 255, 0), (255, 192, 203)), ((255, 255, 0), (0, 255, 127))],
    "Summer": [((255, 165, 0), (0, 191, 255)), ((255, 215, 0), (255, 105, 180))],
    "Autumn": [((255, 140, 0), (139, 69, 19)), ((255, 215, 0), (128, 0, 0))],
    "Winter": [((224, 255, 255), (0, 0, 139)), ((255, 250, 250), (0, 0, 205))]
}
current_theme = "Spring"

# Button debouncing settings
last_button_press_time = 0
BUTTON_DELAY = 500  # Adjust the delay as needed


def setup():
    for y in range(height):
        for x in range(width):
            lifetime[x][y] = 1.0 + random.uniform(0.0, 0.1)
            age[x][y] = random.uniform(0.0, 1.0) * lifetime[x][y]


@micropython.native  # noqa: F821
def draw_background():
    for y in range(height):
        for x in range(width):
            if age[x][y] < lifetime[x][y] * 0.3:
                graphics.set_pen(graphics.create_pen(color[0], color[1], color[2]))
            elif age[x][y] < lifetime[x][y] * 0.5:
                decay = (lifetime[x][y] * 0.5 - age[x][y]) * 5.0
                graphics.set_pen(graphics.create_pen(int(decay * color[0]), int(decay * color[1]), int(decay * color[2])))
            else:
                graphics.set_pen(0)
            graphics.pixel(x, y)


@micropython.native  # noqa: F821
def update_background():
    for y in range(height):
        for x in range(width):
            if age[x][y] >= lifetime[x][y]:
                age[x][y] = 0.0
                lifetime[x][y] = 1.0 + random.uniform(0.0, 0.1)

            age[x][y] += 0.025


def pressed():
    if gu.is_pressed(GalacticUnicorn.SWITCH_A):
        return GalacticUnicorn.SWITCH_A
    if gu.is_pressed(GalacticUnicorn.SWITCH_B):
        return GalacticUnicorn.SWITCH_B
    if gu.is_pressed(GalacticUnicorn.SWITCH_C):
        return GalacticUnicorn.SWITCH_C
    return None


def outline_text(text, x, y):
    graphics.set_pen(0)  # Outline color (black)
    graphics.text(text, x - 1, y - 1, -1, 1)
    graphics.text(text, x, y - 1, -1, 1)
    graphics.text(text, x + 1, y - 1, -1, 1)
    graphics.text(text, x - 1, y, -1, 1)
    graphics.text(text, x + 1, y, -1, 1)
    graphics.text(text, x - 1, y + 1, -1, 1)
    graphics.text(text, x, y + 1, -1, 1)
    graphics.text(text, x + 1, y + 1, -1, 1)

    graphics.set_pen(text_color)  # Set pen back to text color
    graphics.text(text, x, y, -1, 1)


setup()

gu.set_brightness(0.3)

while True:
    current_time = time.ticks_ms()

    if current_time - last_button_press_time >= BUTTON_DELAY:
        if gu.is_pressed(GalacticUnicorn.SWITCH_BRIGHTNESS_UP):
            gu.adjust_brightness(+0.1)
            last_button_press_time = current_time

        if gu.is_pressed(GalacticUnicorn.SWITCH_BRIGHTNESS_DOWN):
            gu.adjust_brightness(-0.1)
            last_button_press_time = current_time

        button_pressed = pressed()

        if button_pressed == GalacticUnicorn.SWITCH_A:
            color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            last_button_press_time = current_time

        elif button_pressed == GalacticUnicorn.SWITCH_B:
            text_color = graphics.create_pen(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            last_button_press_time = current_time

        elif button_pressed == GalacticUnicorn.SWITCH_C:
            themes = list(themed_color_schemes.keys())
            current_theme_index = themes.index(current_theme)
            current_theme = themes[(current_theme_index + 1) % len(themes)]
            color_scheme = random.choice(themed_color_schemes[current_theme])
            text_color, color = color_scheme
            text_color = graphics.create_pen(text_color[0], text_color[1], text_color[2])
            last_button_press_time = current_time

    elapsed_time = time.ticks_diff(current_time, text_start_time) / 1000  # Convert to seconds

    if elapsed_time >= text_durations[current_text_index]:
        current_text_index = (current_text_index + 1) % len(texts)
        text_start_time = current_time

    current_text = texts[current_text_index]
    text_width = graphics.measure_text(current_text, 1)
    max_scale = min(width // text_width, height // 8)
    text_x = (width - text_width * max_scale) // 2
    text_y = (height - 6 * max_scale) // 2

    start = time.ticks_ms()

    draw_background()
    outline_text(current_text, text_x, text_y)
    gu.update(graphics)
    update_background()

    time.sleep(0.001)

    # print("total took: {} ms".format(time.ticks_ms() - start))