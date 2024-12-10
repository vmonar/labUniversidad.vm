class Curso:
    def __init__(self, nombre, codigo, profesor):
        self.nombre = nombre
        self.codigo = codigo
        self.profesor = profesor
    def __str__(self):
        return f"Curso: {self.nombre}, Codigo del curso: {self.codigo}, Profesor: {self.profesor}"