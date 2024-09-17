import sys

color_sets = [
    [255, 255, 255, 'White'],
    [192, 192, 192, 'Silver'],
    [128, 128, 128, 'Gray'],
    [0, 0, 0, 'Black'],
    [255, 0, 0, 'Red'],
    [128, 0, 0, 'Maroon'],
    [255, 255, 0, 'Yellow'],
    [128, 128, 0, 'Olive'],
    [0, 255, 0, 'Lime'],
    [0, 128, 0, 'Green'],
    [0, 255, 255, 'Aqua'],
    [0, 128, 128, 'Teal'],
    [0, 0, 255, 'Blue'],
    [0, 0, 128, 'Navy'],
    [255, 0, 255, 'Fuchsia'],
    [128, 0, 128, 'Purple']
    ]


while True:
    r, g, b = map(int, sys.stdin.readline().split())
    if r == g == b == -1:
        break

    min_ = 10000
    closest_color = None
    for R, G, B, color in color_sets:
        if min_ > ((R - r) ** 2 + (G - g) ** 2 + (B - b) ** 2) ** 0.5:
            min_ = ((R - r) ** 2 + (G - g) ** 2 + (B - b) ** 2) ** 0.5
            closest_color = color
    print(closest_color)