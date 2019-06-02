import os
from PIL import Image
import cv2
import numpy as np


def img_to_arr(path):
	'''
	Convert image at the path given to array
	The returned array will contain RGB tuples
	'''

	img = Image.open(path)
	img = img.resize((300,400))

	return np.array(img, 'uint8')


def arr_to_img(arr):
	'''
	Convert the given array into image
	The given array elements have to contain RGB tuples
	'''

	return Image.fromarray(arr, 'RGB')


def img_mult(matrixa, matrixb):
	'''
	Multiply two given matrices into eachother
	'''

	ans = np.zeros((400,300))

	matrixa = matrixa.tolist()
	matrixb = matrixb.tolist()
	ans = ans.tolist()


	print(len(matrixa))
	for i in range(len(matrixa)):
		for j in range(len(matrixa[0])):
			r = matrixa[i][j][0] * matrixb[i][j][0]
			g = matrixa[i][j][1] * matrixb[i][j][1]
			b = matrixa[i][j][2] * matrixb[i][j][2]
			ans[i][j] = (r%256,g%256,b%256)

	return np.array(ans, 'uint8')


def search_carpet(carpet_path, inventory_dir):
	'''
	Search for similarity among carpets
	Returns a list containing three best matches
	'''

	# carpet = img_to_arr(carpet_path)
	carpet = cv2.imread(carpet_path)
	carpet_hist = cv2.calcHist([carpet],[0],None,[256],[0,256])
	# Transform into 1d array
	# carpet = carpet.flatten()

	directory = inventory_dir
	listdir = os.listdir(directory)

	error_list = list()

	for file in listdir:
		filename = file
		path = os.path.join(directory, filename)
		# this_img = img_to_arr(path).flatten()
		this_img = cv2.imread(path)
		this_img_hist = cv2.calcHist([this_img],[0],None,[256],[0,256])
		# l = min(len(carpet), len(this_img))
		# error_percentage = np.mean(carpet[:l] != this_img[:l])
		error = cv2.compareHist(carpet_hist, this_img_hist, cv2.HISTCMP_CORREL)

		error_list.append([filename, error])

	error_list = np.array(error_list, 'object')
	sorted_percent_col = error_list[:, 1].argsort()[-1:-4:-1]

	best_matches = list()
	for i in sorted_percent_col:
		best_matches.append(os.path.join('/static/outputs', error_list[i][0]))

	return best_matches


def shop_seeker(budget):
	'''
	Search for carpets which can be bought with the budget
	Returns a list of carpets & maxmimum number of carpets can be bought
	'''

	price_list = list()
	with open('prices.csv', 'r') as f:
		lines = list(map(str.strip, f.readlines()))
		for line in lines:
			# print('line')
			# print('============================================')
			# print(line)
			price_list.append([
				line.split(',')[0],
				int(line.split(',')[1])
			])
		print(price_list)

	price_list = np.array(price_list, 'object')
	sorted_index = price_list[:, 1].argsort()

	sum_temp = 0
	carpet_counter = 0

	maxmimum_number = 0

	carpet_list = list()
	prices = list()
	for i in sorted_index:
		print('--------sasasasasas0000000000000---------')
		print(price_list[i])

		if price_list[i][1] > budget:
			continue

		if (sum_temp + int(price_list[i][1])) < budget:
			maxmimum_number += 1


		sum_temp += price_list[i][1]

		carpet_list.append((
			os.path.join('/static/outputs', price_list[i][0]),
			int(price_list[i][1])
		))

		# prices.append(
		# 	int(price_list[i][1])
		# )

	# return carpet_list, prices, maxmimum_number
	return carpet_list, maxmimum_number
