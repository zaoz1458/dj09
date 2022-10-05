from django.urls import path,include
from . import views

app_name="board"

urlpatterns = [
   
    path('index/', views.index,name='index'),
    path('detail/<var>', views.detail,name='detail'),
    path('creply/<var>', views.creply,name='creply'),
    path('dreply/<var1>/<var2>', views.dreply,name='dreply'),
    path('delete/<var>', views.delete,name='delete'),
    path('create', views.create,name='create'),
    path('update/<var>', views.update,name='update'),
    path('likey/<var>', views.likey,name='likey'),
    path('unlikey/<var>', views.unlikey,name='unlikey'),
    
] 
