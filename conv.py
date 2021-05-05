
mat1 = [[1,2,3,4,5,6],[7,8,9,10,11,12],[0,0,1,16,17,18], [0,1,0,7,23,24],[1,7,6,5,4,3]]
kernel = [[1,1,1],[0,0,0],[2,10,3]]
matres = [[0,0,0,0],[0,0,0,0],[0,0,0,0]]
cont1 = 0
cont2 = 0


def convolucion(mat1, mat2, cont1, cont2):	
	a = 0
	b = 0
	c = 0

	for i in range(0,3):
		for j in range(0,3):
			a = mat1[i][j]
			b = mat2[i+cont1][j+cont2]

			c += a*b
	return c


for i in range(0,3):
	for j in range(0,4):
		cont1 = i
		cont2 = j
		matres[i][j] = convolucion(kernel, mat1, cont1, cont2)

print matres