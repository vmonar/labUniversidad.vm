from clases.curso import Curso
from clases.estudiante import Estudiante
from clases.profesor  import Profesor
from clases.universidad  import Universidad

universidad = Universidad("Universidad de el Salvador")

profesor_1 = Profesor("Juan Perez", 30, "M", 202010102, "Matemáticas")
profesor_2 = Profesor("Maria Lopez", 35, "F", 202010103, "Física")
profesor_3 = Profesor("Pedro Ramirez", 40, "M", 202010104, "Química")

Curso_Matemáticas = Curso("Matemáticas", "MAT101", profesor_1)
Curso_Física = Curso("Física", "FIS101", profesor_2)
Curso_Física_2 = Curso("Física 2", "FIS101", profesor_2)
Curso_Química = Curso("Química", "QUI101", profesor_3)

universidad.agregar_curso(Curso_Matemáticas)
universidad.agregar_curso(Curso_Física)
universidad.agregar_curso(Curso_Química)
universidad.agregar_curso(Curso_Física_2)

estudiante_1 = Estudiante("Carlos Perez", 20, "M", 202010101, "Ingeniería en Sistemas Informáticos")

print(universidad)
print(profesor_1)
print(estudiante_1)
print(Curso_Matemáticas)