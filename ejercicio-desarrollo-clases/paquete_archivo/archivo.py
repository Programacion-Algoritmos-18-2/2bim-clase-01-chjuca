
import codecs                                           # Importamos codecs

class ArchivoLeer:                                      # Creamos la clase ArchivoLeer
    
    def __init__(self):                                 # Constructor de la clase
        self.archivo = codecs.open("data/notas.csv", "r")   # Abrimos el archivo csv que se encuentra en la carpeta data

    def obtener_informacion(self):                      # Metodo Obtener_Informacion que devuelve el contenido del archivo
        return self.archivo.readlines()

    def cerrar_archivo(self):                           # Metodo que cierra el Archivo
        self.archivo.close()


class ArchivoEscribir:                                  # Creamos una clase llamada ArchivoEscribir
    def __init__(self):                                 # Constructor de la clase  
        self.archivo = codecs.open("data/promedio.csv", "a")    # Abrimos el csv de nombre promedio

    def agregar_informacion(self, p):                   # Metodo que agrega informacion al archivo
        self.archivo.write("%s|%.2f\n" % (p.getNombre(),p.promedio()))  # al archivo que tenemos abierto lo enviamos la cadena con el nombre de la persona y el promedio 

    def cerrar_archivo(self):                           # Metodo para cerrar el archivo
        self.archivo.close()                            # Cerramos el archivo
