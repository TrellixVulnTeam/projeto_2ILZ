from django.db import models
# Create your models here.
class Curso(models.Model):

    sigla = models.CharField(max_length=5)
    nome = models.CharField(max_length=200)
    tipo = models.CharField(max_length=50, blank=True)
    carga_horaria = models.IntegerField(default=1000)
    ativo = models.BooleanField(default=True)

    descricao = models.TextField(blank=True)

    def __str__(self):
        return self.nome