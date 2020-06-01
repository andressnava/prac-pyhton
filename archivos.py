from io import *
import pickle

def insertarUsuario(correo, usuarioNombre, password):
	nuevoRegistro = open("registros.txt", "a")
	cadenaUsuario = "\n{}\t\t{}\t\t{}\n".format(correo, usuarioNombre, password)
	nuevoRegistro.write(cadenaUsuario)
	nuevoRegistro.close()


def imprimirUsuarios(self):
	leerRegistro = open("registros.txt", "r")
	print(leerRegistro.read())
	leerRegistro.close()

def eliminarRegistro(self):
	registro = open("registros.txt", "w")
	registro.write("")
	registro.close()

def codificarUsuarios(self):
	lectura = open("registros.txt", "r")
	informacionGuardada = lectura.read()

	escribirRespaldo = open("Respaldo", "wb")
	pickle.dump(informacionGuardada, escribirRespaldo)

	lectura.close()
	escribirRespaldo.close()

def leerCodificacion(self):
	lecturabinaria = open("Respaldo", "rb")
	informacion = pickle.load(lecturabinaria)
	print(informacion)

	#lecturabinaria.close()

