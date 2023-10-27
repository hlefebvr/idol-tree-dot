WHITE = (255, 255, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (0, 0, 255)

def scale(value, min, max):
    return (value - min) / (max - min + 1e-10)

def get_color_between(from_rgb, to_rgb, score):

    r1, g1, b1 = from_rgb
    r2, g2, b2 = to_rgb
    r = int(r1 + (r2 - r1) * score)
    g = int(g1 + (g2 - g1) * score)
    b = int(b1 + (b2 - b1) * score)

    return (r, g, b)

def as_hex(rgb):
    r,g,b = rgb
    return "#{:02x}{:02x}{:02x}".format(r, g, b)
