import time
import random
from galactic import GalacticUnicorn
from picographics import PicoGraphics, DISPLAY_GALACTIC_UNICORN as DISPLAY

'''
Displays outlined text with random colors on a blinking background.

- A button: Randomizes background color.
- B button: Randomizes text color.
- LUX +/-: Adjusts brightness.
'''

gu = GalacticUnicorn()
graphics = PicoGraphics(DISPLAY)

width = GalacticUnicorn.WIDTH
height = GalacticUnicorn.HEIGHT

# Text settings
text = "EXAMPLE"
text_color = graphics.create_pen(255, 255, 255)  # Initial white text

# Set larger font
graphics.set_font("bitmap8")

# Calculate text position for maximum size
text_width = graphics.measure_text(text, 1)
max_scale = min(width // text_width, height // 8)
text_x = (width - text_width * max_scale) // 2
text_y = (height - 6 * max_scale) // 2

# Blinking background settings
color = (255, 0, 0)  # Initial red background
lifetime = [[0.0 for y in range(height)] for x in range(width)]
age = [[0.0 for y in range(height)] for x in range(width)]


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
    # ... (other button checks if needed)
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

gu.set_brightness(0.5)

while True:

    if gu.is_pressed(GalacticUnicorn.SWITCH_BRIGHTNESS_UP):
        gu.adjust_brightness(+0.01)

    if gu.is_pressed(GalacticUnicorn.SWITCH_BRIGHTNESS_DOWN):
        gu.adjust_brightness(-0.01)

    # Check for button presses
    button_pressed = pressed()

    if button_pressed == GalacticUnicorn.SWITCH_A:
        # Randomize background color
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    elif button_pressed == GalacticUnicorn.SWITCH_B:
        # Randomize text color
        text_color = graphics.create_pen(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    start = time.ticks_ms()

    # Draw background
    draw_background()

    # Draw outlined text on top of the background
    outline_text(text, text_x, text_y)

    gu.update(graphics)

    update_background()

    time.sleep(0.001)

    print("total took: {} ms".format(time.ticks_ms() - start))
