

def validarCorreo(correo):
	i = 0
	contadorArroba = 0
	contadorPunto = 0
	posicionArroba = 0

	while i < len(correo):

		if "@" in correo[i]:
			contadorArroba = contadorArroba + 1
			posicionArroba = i
	
		if "." in correo[i] and posicionArroba < i and contadorArroba == 1:
			contadorPunto = contadorPunto + 1

		i = i + 1

	if contadorArroba == 1 and contadorPunto == 1:
		print("El correo es valido")
		return True
	else:
		print("Algo salio mal\nIntenta de nuevo")
		return False

