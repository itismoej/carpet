from PIL import Image
import numpy as np


def img_to_arr(path):
	'''
	Convert image at the path given to array
	The returned array will contain RGB tuples
	'''

	img = Image.open(path)

	width, height = img.size
	if width != 300 or height != 400:
		img = img.resize((300,400))

	return np.array(img)


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

	ans = matrixa.copy()

	print(len(matrixa))
	for i in range(len(matrixa)):
		for j in range(len(matrixa[0])):
			r = matrixa[i][j][0] * matrixb[i][j][0]
			g = matrixa[i][j][1] * matrixb[i][j][1]
			b = matrixa[i][j][2] * matrixb[i][j][2]
			ans[i][j] = (r%256,g%256,b%256)

	return ans
