from django.db import models

class Contato(models.Model):
  created = models.DateTimeField(auto_now_add=True)
  nome = models.CharField(max_length=100, blank=True, default='')
  idade = models.CharField(max_length=3, blank=True, default='')
  telefone = models.CharField(max_length=13, blank=True, default='')
  endereco = models.TextField()

  class Meta:
    ordering = ['created']
