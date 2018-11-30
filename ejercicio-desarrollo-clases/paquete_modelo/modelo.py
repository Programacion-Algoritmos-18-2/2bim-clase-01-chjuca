class Persona(object):                          # Creamos el objeto Persona
    
    def __init__(self, n, nota1,nota2,nota3):   # Constructor del objeto persona

        self.nombre = n                         # Atributos del objeto Persona
        self.nota1 = int(nota1)
        self.nota2 = int(nota2)
        self.nota3 = int(nota3)

    def setNombre(self, n):                     # Metodos Set
        self.nombre = n

    def setNota1(self, nota1):
        self.nota1 = nota1

    def setNota2(self, nota2):
        self.nota2 = nota2

    def setNota3(self, nota3):
        self.nota3 = nota3

    def getNombre(self):                        # Metodos Get
        return self.nombre

    def getNota1(self):
        return self.nota1

    def getNota2(self):
        return self.nota2

    def getNota3(self):
        return self.nota3

    def promedio(self):                         # Metodo para calcular el promedio
        return (self.nota1+self.nota2+self.nota3)/3

    
    def __str__(self):                          # Metodo toString de la clase 
        return "%s|%f\n" % (self.nombre, self.promedio())
