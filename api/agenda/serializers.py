from rest_framework import serializers
from agenda.models import Contato
from django.contrib.auth.models import User


class ContatoSerializer(serializers.ModelSerializer):
  log = serializers.ReadOnlyField(source='log.username')
  class Meta:
    model = Contato
    fields = ['id', 'nome', 'idade', 'telefone', 'endereco','log']

class UserSerializer(serializers.ModelSerializer):
  contatos = serializers.PrimaryKeyRelatedField(many=True, queryset=Contato.objects.all())
  class Meta:
    model = User
    fields = ['id','username', 'contatos']
