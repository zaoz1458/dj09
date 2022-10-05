from django.urls import path,include
from . import views

app_name="votes"

urlpatterns = [
    path('index/', views.index,name='index'),
    path('detail/<var>', views.detail,name='detail'),
    path('votes/<var>', views.votes,name='votes'),
    path('create', views.create,name='create'),
    path('cancel/<var>', views.cancel,name='cancel'),
    
]
