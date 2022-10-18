from django.core.validators import RegexValidator
from django.db import models
from django.utils.timezone import now


class Formul(models.Model):
    carne = models.TextField(validators=[RegexValidator(regex='^[A|a][a-zA-Z0-9][5][a-zA-Z0-9][a-zA-Z0-9][1|3|9]$', message='Length has to be 6', code='nomatch')])
    name = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    genero = models.CharField(max_length=50)
    tel= models.IntegerField()
    born = models.DateField()
    carrera = models.CharField(max_length=50)
    poesia = models.CharField(max_length=50)
    insc = models.DateTimeField()
    

    def __str__(self):
        return self.carne
    
class Formul2(models.Model):
    carne = models.TextField(validators=[RegexValidator(regex='^[A|a][a-zA-Z0-9][5][a-zA-Z0-9][a-zA-Z0-9][1|3|9]$', message='Length has to be 6', code='nomatch')],primary_key = True)
    name = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    genero = models.CharField(max_length=50)
    tel= models.IntegerField()
    born = models.DateField()
    carrera = models.CharField(max_length=50)
    poesia = models.CharField(max_length=50)    
    insc = models.DateTimeField(default=now, editable=False)
    

    def __str__(self):
        return self.carne