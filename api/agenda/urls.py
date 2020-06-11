from django.urls import path
from django.conf.urls import include
from agenda import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView, TokenVerifyView
    )

urlpatterns = [
  path('contatos/', views.AgendaList.as_view()),
  path('contatos/<int:pk>/', views.AgendaDetail.as_view()),
  path('users/', views.UserList.as_view()),
  path('users/<int:pk>/', views.UserDetail.as_view()),
  path('api-auth/', include('rest_framework.urls')),
  path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
  path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
  path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
