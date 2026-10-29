import math
from PIL import Image, ImageDraw

WIDTH, HEIGHT = 400, 400
FRAMES = 40
BALL_RADIUS = 30


def make_frame(i):
    t = i / FRAMES
    img = Image.new("RGB", (WIDTH, HEIGHT), "#1e1e2e")
    draw = ImageDraw.Draw(img)

    # Bola quicando (movimento senoidal) com cor que muda ao longo do tempo
    x = WIDTH * t
    y = HEIGHT / 2 + math.sin(t * 2 * math.pi * 2) * 120
    color = (
        int(127 + 127 * math.sin(t * 2 * math.pi)),
        int(127 + 127 * math.sin(t * 2 * math.pi + 2)),
        int(127 + 127 * math.sin(t * 2 * math.pi + 4)),
    )
    draw.ellipse(
        (x - BALL_RADIUS, y - BALL_RADIUS, x + BALL_RADIUS, y + BALL_RADIUS),
        fill=color,
    )

    # Círculo girando no centro
    cx, cy = WIDTH / 2, HEIGHT / 2
    angle = t * 2 * math.pi
    px = cx + math.cos(angle) * 80
    py = cy + math.sin(angle) * 80
    draw.ellipse((px - 10, py - 10, px + 10, py + 10), fill="white")

    return img


frames = [make_frame(i) for i in range(FRAMES)]
frames[0].save(
    "animation.gif",
    save_all=True,
    append_images=frames[1:],
    duration=50,  # ms por frame
    loop=0,  # repete para sempre
)
print("GIF salvo em animation.gif")
