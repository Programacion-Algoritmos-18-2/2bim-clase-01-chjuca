"""
    Manejo de Excepciones
"""

class MiError(Exception):
    """
    """

    def __init__(self, valor):
        self.valor = valor

    def __str__(self):
        return "Error, para el valor ingresado, debe ser mayor a 20 %s" %(self.valor)
