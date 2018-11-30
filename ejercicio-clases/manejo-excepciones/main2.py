"""
	Ejemplos de Manejo de Excepciones
"""

try:
	num1=input("Ingrese un numero: ")
	num1=int(num1)
	num2=input("Ingrese otro numero: ")
	num2=int(num2)
	operacion = num1/num2
	print("El valor de la suma es: %d "%(operacion))
	
except ValueError as e:
	print("Existe un error(%s): %s!" % (e.__class__,e))

except NameError as e:
	print("Existe un error (%s): %s!" % (e.__class__, e))

except ZeroDivisionError as e:
	print("Existe un error (%s): %s!" % (e.__class__, e))
"""
except Exception as e:
	print("Existe un error (%s): %s" %(e.__class__,e))
	"""

