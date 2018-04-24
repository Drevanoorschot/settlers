from math import sqrt

frame_resolution = (1000, 1000)

tile_resolution = (180, 155)

x_offset = 150
y_offset = 150
x_distance = 2 * (sqrt(3) / 2 * tile_resolution[1]) / 8
y_distance = tile_resolution[1] / 4
x_token_offset = tile_resolution[0] / 2
y_token_offset = tile_resolution[1] / 2

token_radius = 20
token_border_radius = 5