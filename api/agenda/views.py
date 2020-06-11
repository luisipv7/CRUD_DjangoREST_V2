from django.shortcuts import render
from agenda.models import Contato
from agenda.serializers import ContatoSerializer
from agenda.serializers import UserSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from agenda.permissions import IsOwnerOrReadOnly


class AgendaList(generics.ListCreateAPIView):
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]
  queryset = Contato.objects.all()
  serializer_class = ContatoSerializer
  def perform_create(self, serializer):
    serializer.save(log=self.request.user)


class AgendaDetail(generics.RetrieveUpdateDestroyAPIView):
  permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
  queryset = Contato.objects.all()
  serializer_class = ContatoSerializer

class UserList(generics.ListAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer
