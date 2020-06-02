from objetos import *

print("-----------------------------------------")
print("			R e g i s t r a t e				")
print("-----------------------------------------")

print("\n1)Usuario común\n2)Administrador\n9)Salir")


while True:

	while True:
		try:
			opcion = int(input("\nElige una opción: "))
			break
		except ValueError:
			print ("El valor es invalido, intenta de nuevo")

	if opcion == 1:

		correo = input("\nCorreo electronico: ")
		nombreUsuario = input("Nombre de usuario: ")
		password = input("Contraseña: ")
		generarUsuario(correo, nombreUsuario, password)
		break

	elif opcion == 2:

		correo = input("\nCorreo electronico: ")
		nombreUsuario = input("Nombre de usuario: ")
		password = input("Contraseña: ")
		clave = input("Clave: ")
		generarAdministrador(correo, nombreUsuario, password, clave)
		break

	elif opcion == 9:

		print("Hasta Luego!!!")
		break

	else:
		print("Opción incorrecta, intenta nuevamente")


