
import numpy as np

#matriz para poder probar el codigo
mat1 = np.array([[1,2],[3,4]])

#funcion para agregar padding, recibe la matriz y la dimension del padding que se desea agregar
def padding (mat1, pad):

	row, col = mat1.shape

	row2 = 0
	col2 = 0

	#definen las dimensiones de la matriz con el padding
	row2 = row + 2*pad
	col2 = col + 2*pad

	matres = np.zeros((row2, col2))

	#ciclo que llena matres a partir del padding que fue indicado
	for i in range(pad, row2-pad):
		for j in range(pad, col2-pad):
			matres[i][j] = mat1[i-pad][j-pad]

	return matres

print padding(mat1, 1)
