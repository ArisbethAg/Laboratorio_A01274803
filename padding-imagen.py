import numpy as np
import cv2
import matplotlib.pyplot as plt
import argparse

def padding (image, pad, verbose=False):

	if len(image.shape) == 3:
		print("Found 3 Channels : {}".format(image.shape))
		image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		print("Converted to Gray Channel. Size : {}".format(image.shape))
	else:
		print("Image Shape : {}".format(image.shape))


	row, col = image.shape

	row2 = 0
	col2 = 0

	row2 = row + 2*pad
	col2 = col + 2*pad

	matres = np.zeros((row2, col2))

	for i in range(pad, row2-pad):
		for j in range(pad, col2-pad):
			matres[i][j] = image[i-pad][j-pad]

	if verbose:
		plt.imshow(matres, cmap='gray')
		plt.title("Padded Image")
		plt.show()

	return matres


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True, help="Path to the image")
    args = vars(ap.parse_args())
    image = cv2.imread(args["image"]) 

print (padding(image, 1, verbose=True))