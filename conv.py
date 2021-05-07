
import numpy as np

#matrices para poder probar el codigo
mat1 = np.array([[1,2,3,4,5,6],[7,8,9,10,11,12],[0,0,1,16,17,18], [0,1,0,7,23,24],[1,7,6,5,4,3]])
kernel = np.array([[1,1,1],[0,0,0],[2,10,3]])
matres = np.array([[0,0,0,0],[0,0,0,0],[0,0,0,0]])


#funcion para realizar la convolucion de una matriz a partir de un kernel
def convolucion(mat1, mat2):	

	c = 0
	row1, col1 = mat1.shape 

	for i in range(0, row1):
		for j in range(0, col1):
			c += mat1[i][j]*mat2[i][j]

	return c

#funcion para poder desplazar la funcion de convolucion en la matriz
def desp_convolucion(img, kernel):

	row2, col2 = matres.shape
	row3, col3 = kernel.shape

	for i in range(0, row2):
		for j in range(0, col2):
			matres[i][j] = convolucion(img[i: i + row3, j: j + col3], kernel)

	return matres

desp_convolucion (mat1, kernel)

print matres