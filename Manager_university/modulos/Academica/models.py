from django.db import models

class Carrera(models.Model):
    codigo = models.CharField(max_length=3, primary_key=True)
    nombre = models.CharField(max_length=55)
    duracion = models.PositiveSmallIntegerField(default=5)

    def __str__(self):
        txt = "{0} (duracion: {1} año(s))"
        return txt.format(self.nombre, self.duracion)

class Estudiante(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    PrimerApellido = models.CharField(max_length=30)
    SegundoApellido = models.CharField(max_length=30)
    nombres = models.CharField(max_length=30)
    FechaNacimiento = models.DateField()
    sexos = [
        ('M', 'Masculino'),
        ('F', 'Femenino')
    ]
    sexo = models.CharField(max_length=1, choices=sexos, default='F')
    carrera = models.ForeignKey(Carrera, null=False, blank=False, on_delete=models.CASCADE)
    vigencia = models.BooleanField(default=True)


def nombre_completo(self):
    texto = "{0} {1}, {2}"
    return texto.format(self.PrimerApellido, self.SegundoApellido, self.nombres)


def __str__(self):
    txt = "{0} / Carrera: {1} / {2}"
    if self.vigencia: 
        estadoEstudiante = "Vigente"
    else:
        estadoEstudiante = "NoVigente"
    return txt.format(self.nombre_completo(), self.Carrera, estadoEstudiante)


class Curso(models.Model):
    codigo = models.CharField(max_length=8, primary_key=True)
    nombre = models.CharField(max_length=35)
    creditos = models.PositiveSmallIntegerField()
    docente = models.CharField(max_length=85)

    def __str__(self):
        txt = "{0} ({1}) / Docente: {2}"
        return txt.format(self.nombre, self.codigo, self.docente)

class Matricula(models.Model):
    identificacion = models.AutoField(primary_key=True)
    estudiante = models.ForeignKey(Estudiante, null=False, blank=False, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, null=False, blank=False, on_delete=models.CASCADE)
    fecha_matricula = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        txt = "{0} matriculad{1} en el curso {2} / Fecha: {3}"
        if self.estudiante.sexo == 'F':
            letrasexo = "a"
        else:
            letrasexo = "o"

        fecMat = self.fecha_matricula.strftime("%A %d/%m/%Y %H:%M:%S")
        return txt.format(self.estudiante.nombre_completo(), letrasexo, self.curso, fecMat)