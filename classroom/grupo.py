from classroom.asignatura import Asignatura

class Grupo:
    grado = "Grado 12"

    def __init__(self, grupo="grupo predeterminado", asignaturas=None, estudiantes=None):
      self._grupo = grupo
      self._asignaturas = asignaturas if asignaturas else []
      self.listadoAlumnos = estudiantes if estudiantes else []


    def listadoAsignaturas(self, **kwargs):
        for x in kwargs.values():
            self._asignaturas.append(Asignatura(x))

    def agregarAlumno(self, alumno, lista=None):
        nueva_lista = list(lista) if lista else []  
        nueva_lista.append(alumno) 
        self.listadoAlumnos += nueva_lista 
    def __str__(self):
        return "Grupo de estudiantes: " + self._grupo 

    @ classmethod
    def asignarNombre(cls, nombre="Grado 10"):
        cls.grado = nombre

    @ classmethod
    def asignarNombre(cls, nombre="Grado 4"):
        cls.grado = nombre
    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre
