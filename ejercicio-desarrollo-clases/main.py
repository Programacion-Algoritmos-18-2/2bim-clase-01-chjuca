from paquete_archivo.archivo import *			# Importamos al modulo archivo
from paquete_modelo.modelo import *				# Importamos el modulo modelo

ml=ArchivoLeer()								# instanciamos un objeto de tipo ArchivoLeer
me=ArchivoEscribir()							# intanciamos un objeto de tipo ArchivoEscribir
lista = ml.obtener_informacion()				# creaos una lista que obtendra el texto que se encuentra en el archivo csv
lista = [l.split("|") for l in lista]			# Dividimos la cadena por el separador "|"
lista = lista[1:]								# Omitimos el encabezado y trabajamos la lista desde la posicion 1
for d in lista:									# ciclo que recorrera la lista
	p = Persona(d[0], d[1], d[2], d[3])			# Creamos un objeto de tipo persona y le enviamos los parametos correspondientes
	print(p)									# Imprimimos el obejto creado
	me.agregar_informacion(p)					# Agregamos a un archivo csv la informacion obtenida

ml.cerrar_archivo()								# Cerramos el archivo 
me.cerrar_archivo()								# Cerramos el archivo nuevo

