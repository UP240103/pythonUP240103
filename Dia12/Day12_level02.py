import random

def list_of_rgb_colors(n):
    colors = []
    for _ in range(n):
        colors.append(f"rgb({random.randint(0,255)}, {random.randint(0,255)}, {random.randint(0,255)})")
    return colors

print(list_of_rgb_colors(3))

