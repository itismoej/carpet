from random import sample

colors_of_carpet_areas = {}

INF=9999999


def color_possibility_for_area(carpet_adjacent_parts, carpet_area_number, color):
	'''
	Check Whether Given Color Can Be Assigned To Current Area Or Not
    '''

	for neighbor_area in carpet_adjacent_parts.get(carpet_area_number):
		color_of_neighbor = colors_of_carpet_areas.get(neighbor_area)
		if color_of_neighbor == color:
			return False

	return True


def assign_color_to_area(carpet_adjacent_parts, carpet_area_number, available_colors):
	'''
	Assign A Color To Given Carpet Area From Available Colors
	'''


	for color in available_colors:
		if color_possibility_for_area(carpet_adjacent_parts, carpet_area_number, color):
			return color


def color_carpet_areas(carpet_adjacent_parts, available_colors):
	'''
	Color Carpet Areas With Minimum Number Of Colors
	'''

	global colors_of_carpet_areas

	available_colors=sample(available_colors,len(available_colors))

	for carpet_part_num in carpet_adjacent_parts:
		colors_of_carpet_areas[carpet_part_num] = assign_color_to_area(carpet_adjacent_parts, carpet_part_num,available_colors)

	return colors_of_carpet_areas


def find_nearest_vertex(number_of_vertices, vertices_distances, included_vertices_sp):
	'''
	find the nearest unvisited vertex
	'''

	min_distance=INF

	min_vertex_number=int()

	for vertex in range(number_of_vertices):
		if vertices_distances[vertex] < min_distance and included_vertices_sp[vertex] == False:
			min_distance = vertices_distances[vertex]
			min_vertex_number = vertex

	return min_vertex_number


def dijkstra(city_junctions_array, number_of_vertices, current_location):

	visited_vertices = [-1] * (number_of_vertices)

	vertices_distances = [INF] * number_of_vertices
	vertices_distances[current_location] = 0
	list_not_included_vertices = [False] * number_of_vertices

	for i in range(number_of_vertices):

		u = find_nearest_vertex(number_of_vertices, vertices_distances, list_not_included_vertices)

		list_not_included_vertices[u] = True

		for v in range(number_of_vertices):
			if city_junctions_array[u][v] > 0 and list_not_included_vertices[v] == False and vertices_distances[v] > vertices_distances[u] + city_junctions_array[u][v]:
				vertices_distances[v] = vertices_distances[u] + city_junctions_array[u][v]
				visited_vertices[v]=u



	return  vertices_distances,visited_vertices


def print_path_to_branch(visited_vertices, branch_number, path_to_show):

	if visited_vertices[branch_number] == -1:
		path_to_show+=str(branch_number)
		return path_to_show

	t=print_path_to_branch(visited_vertices, visited_vertices[branch_number], path_to_show)
	path_to_show += ''.join(reversed(list(str(branch_number)))) + ' >- ' + t
	return (path_to_show)


def nearest_company_branch_distance(city_junctions_array, current_location, list_of_company_branch):
	'''
	Find Shortest Path From Current Location To All Company Branches
	'''

	if current_location in list_of_company_branch:
		return 0,0

	number_of_vertices=len(city_junctions_array)

	all_shortest_paths,visited_vertices=dijkstra(city_junctions_array, number_of_vertices, current_location)

	nearest_branch_distance=INF
	nearest_branch_number=int()


	for branch in list_of_company_branch:
		if all_shortest_paths[branch] < nearest_branch_distance:
			nearest_branch_distance=all_shortest_paths[branch]
			nearest_branch_number=branch


	route=(print_path_to_branch(visited_vertices,nearest_branch_number,""))[::-1]
	return (nearest_branch_distance,route)


# h = [
# 		[0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# 		[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# 		[0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
# 		[1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
# 		[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
# 		[0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
# 		[0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
# 		[0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0],
# 		[0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0],
# 		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
# 		[0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
# 		[0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
# 		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
# ]
# print(nearest_company_branch_distance(h, 1, [10, 6, 12]))


# colors = ["red", "black", "brown", "blue", "green"]

# carpet_areas = {
# 	0:  [1, 3],
# 	1:  [0],
# 	2:  [4],
# 	3:  [0, 5],
# 	4:  [2, 7],
# 	5:  [3, 7],
# 	6:  [8],
# 	7:  [4, 5, 8],
# 	8:  [6, 7, 10],
# 	9:  [10, 11],
# 	10: [8, 9],
# 	11: [9, 12],
# 	12: [11],
# }

# node_colors = color_carpet_areas(carpet_areas, colors)

# print('number of colors:', len(set(node_colors.values())))
# print('----------')

# for key, value in node_colors.items():
# 	print(key, value)

