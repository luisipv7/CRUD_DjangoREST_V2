from django.urls import path
from agenda import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
  path('contatos/', views.AgendaList.as_view()),
  path('contatos/<int:pk>/', views.AgendaDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
