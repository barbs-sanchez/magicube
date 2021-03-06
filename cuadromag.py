def es_magico (matriz) :
	# tamaÃ±o de las matrices (matriz es NxN)
	N = len(matriz[0])
	# arreglo para guardar las sumas y poder verificarlas luego
	sumas = []
	# sumar filas
	for i in range (N) :
		suma = 0
		for j in range (N) :
			suma += matriz[i][j]
		sumas.append (suma)
	# sumar columnas
	for j in range (N) :
		suma = 0
		for i in range (N) :
			suma += matriz[i][j]
		sumas.append (suma)
	# sumar diagonal arriba -> abajo
	suma = 0
	for k in range (N):
		suma += matriz[k][k]
	sumas.append (suma)
	# sumar diagonal abajo -> arriba
	suma = 0
	for j in range (N):
		i = N - 1 - j
		suma += matriz[i][j]
	sumas.append (suma)
	# verificar que las sumas sean iguales y retornar
	ultimaSuma = sumas[0]
	for suma in sumas :
		if ultimaSuma != suma :
			return False
		ultimaSuma = suma
	return True