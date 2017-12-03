import math

starting_point = 12

#to find out which layer you're on:
	#take the square root of starting point
	#round up to the nearest odd number
	#that number is the dimension of your matrix

def find_layer(start):
	square_root = math.ceil(math.sqrt(start))
	if square_root % 2 == 1:
		layer_number = square_root
	else:
		layer_number = square_root + 1
	return int(layer_number)


def find_starting_coor(layer, start):
	top_left = layer**2 - 2*(layer - 1)
	top_right = layer**2 - 3*(layer - 1)
	bottom_left = layer**2 - (layer - 1)
	bottom_right = layer**2
	if start < top_right:
		starting_x = layer - 1
		starting_y = top_right - start
	elif start < top_left:
		starting_x = top_left - start
		starting_y = 0
	elif start < bottom_left:
		starting_x = 0
		starting_y = start - top_left
	elif start < bottom_right:
		starting_x = start - bottom_left
		starting_y = layer - 1
	return starting_x, starting_y

def find_destination_coor(layer_number):
	destination_x = (layer_number/2)
	destination_y = (layer_number/2)
	return destination_x, destination_y

def find_manhattan(starting_coor, destination_coor):
	absolute_x = abs(starting_coor[0]-destination_coor[0])
	absolute_y = abs(starting_coor[1]-destination_coor[1])
	manhattan_dist = absolute_x + absolute_y
	return manhattan_dist

layer_no = find_layer(starting_point)
print layer_no
starting_coord = find_starting_coor(layer_no, starting_point)
print starting_coord
destination_coord = find_destination_coor(layer_no)
print destination_coord
answer = find_manhattan(starting_coord, destination_coord)
print answer




	