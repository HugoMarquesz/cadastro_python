from django.db import models
from cpf_field.models import CPFField

class Usuario(models.Model) :
  email = models.EmailField( max_length=254)
  cpf = CPFField('cpf')

  def __str__(self) :
    return self.email