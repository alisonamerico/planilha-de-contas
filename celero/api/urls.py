from django.urls import path

from celero.api import views

app_name = 'api'
urlpatterns = [
    path('', views.ListContabilidade.as_view()),
    path('<int:pk>/', views.DetailContabilidade.as_view()),
]
