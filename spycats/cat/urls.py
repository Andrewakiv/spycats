from django.urls import path
from . import views

app_name = 'cat'

urlpatterns = [
    path('cats/', views.CatList.as_view(), name='cats-list'),
    path('cats/<pk>/', views.CatDetail.as_view(), name='cats-detail'),
]
