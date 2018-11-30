"""
	Ejemplos de Manejo de Excepciones
"""

try:
	edad=input("Ingrese su edad: ")
	edad=int(edad)
	print("Su edad es: %d"%(edad))
	
except ValueError as e:
	print("Existe un error(%s): %s!" % (e.__class__,e))

except NameError as e:
	print("Existe un error (%s): %s!" % (e.__class__, e))
"""
except Exception as e:
	print("Existe un error (%s): %s" %(e.__class__,e))
	"""

