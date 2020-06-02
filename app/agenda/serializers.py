from rest_framework import serializers
from agenda.models import Contato


class ContatoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Contato
    fields = ['id', 'nome', 'idade', 'telefone', 'endereco']
