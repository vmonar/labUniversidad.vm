class Universidad:
    def __init__(self, nombre):
        self.nombre = nombre
        self.curso = []
    def agregar_curso(self, curso):
        self.curso.append(curso)
    def __str__(self):
        curso_str = "\n".join([str(curso) for curso in self.curso])
        return f"Universidad: {self.nombre}\nCursos:\n{curso_str}"