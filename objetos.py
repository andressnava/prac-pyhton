from validacion import *
from archivos import *

class Usuario():
	def __init__(self, correo,usuarioNombre, password):
		self.correo = correo
		self.usuarioNombre = usuarioNombre
		self.password = password

	def sesion_exitosa(self):
		print("Bienvenido ",  self.usuarioNombre, "la sesión ha iniciado exitosamente")

	def privilegios(self):
		print("Usuario normal, no puedes hacer modificaciones")

class Administrador(Usuario):

	def __init__(self, correo, usuarioNombre, password, clave):
		super().__init__(correo, usuarioNombre, password)
		self.clave = clave

	def privilegios(self):
		print("Tienes todos los privilegios")

	def registroSesion(self):
		imprimirUsuarios(self)

	def respaldarUsuarios(self):
		codificarUsuarios(self)

	def leerRespaldo(self):
		leerCodificacion(self)

	def eliminarUsuarios(self):
		eliminarRegistro(self)

def generarUsuario(correo, usuarioNombre, password):

	condicion = validarCorreo(correo)

	if condicion == True:

		nuevoUsuario = Usuario(correo, usuarioNombre, password)
		insertarUsuario(correo, usuarioNombre, password)
		nuevoUsuario.sesion_exitosa()
		nuevoUsuario.privilegios()

	elif condicion == False:

		print("Hay algun error")


def generarAdministrador(correo, usuarioNombre, password, clave):

	condicion = validarCorreo(correo)

	if condicion == True and clave == "admin":

		nuevoAdministrador = Administrador(correo, usuarioNombre, password, clave)
		insertarUsuario(correo, usuarioNombre, password)
		nuevoAdministrador.sesion_exitosa()
		nuevoAdministrador.privilegios()

		while True:
			eleccion = int(input("\n1)Consultar Usuarios\t2)Hacer respalso\t3)Leer respaldo\t4)Eliminar Usuarios\t9)Salir\nElección: "))
			if eleccion == 1:
				nuevoAdministrador.registroSesion()
				break
			elif eleccion == 2:
				nuevoAdministrador.respaldarUsuarios()
				print("Se ha respaldado con exito !!!")
				break
			elif eleccion == 3:
				nuevoAdministrador.leerRespaldo()
				break
			elif eleccion == 4:
				print("¿Estas seguro que quieres eliminar el registro?")
				opcion = int(input("       [1 = Si]         [2 = No]\nR:"))
				if opcion == 1:
					nuevoAdministrador.eliminarUsuarios()
				elif opcion == 2:
					pass
				break
			elif eleccion == 9:
				print("Hasta Luego !!!!")
				break
			else:
				print("Opción incorrecta")

	elif condicion == False:

		print("Hay algun error")

	elif clave != "admin" and condicion == True:
		print("Clave incorrecta")