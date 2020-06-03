from django.shortcuts import render
from agenda.models import Contato
from agenda.serializers import ContatoSerializer
from rest_framework import generics


class AgendaList(generics.ListCreateAPIView):
  queryset = Contato.objects.all()
  serializer_class = ContatoSerializer


class AgendaDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Contato.objects.all()
  serializer_class = ContatoSerializer
