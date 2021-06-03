from django.urls import path
from . import views


app_name = 'superheroes'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:superheroes_id>/', views.detail, name='detail'),
    path('new/', views.create, name='create_new_superhero')
]
