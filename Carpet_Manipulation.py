# import PIL
# im = PIL.Image.open('ss.jpg', 'r')
# pix_val = list(im.getdata())
# # area=(100,100,200,200)
# # ss=im.crop(area)
#
# for i in range(1000):
# 	pix_val[i]=(200,200,200)
# tt=[[200,200,200],[200,200,200]]
# img = PIL.Image.fromarray(tt, 'RGB')
#
#
# img.show()
#

from PIL import Image
import numpy

def Convert_Image_To_Array_Of_Pixels(File_Path):

	'''

	Function To Convert An Image To (Numpy) Array Of Size 300 * 400

	#TODO Resize To 300*400??
	'''


	Selected_Image = Image.open(File_Path)

	Image_Pixel_Array = (numpy.array(Selected_Image))

	return Image_Pixel_Array





print(Convert_Image_To_Array_Of_Pixels('ss.jpg'))






#
# new_matrix=[]
#
# for i in range(374,-1,-1):
# 	new_matrix.append(np_im[i])

# np_im=numpy.array(new_matrix)
# for j in range(100):
# 	for i in range(500):
# 		np_im[j][i] = [200, 200, 200]


# new_im = Image.fromarray(np_im)
# new_im.save("numpy_altered_sample3.png")


# im.save("22.jpg")