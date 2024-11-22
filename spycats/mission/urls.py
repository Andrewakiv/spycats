from django.urls import path
from . import views

app_name = 'mission'

urlpatterns = [
    path('missions/', views.MissionList.as_view(), name='misssions-list'),
    path('missions/<int:pk>/', views.MissionDetail.as_view(), name='misssions-detail'),
    path('missions/<int:pk>/delete/', views.MissionDelete.as_view(), name='delete-mission'),
    path('missions/<int:pk>/assign-cat/', views.AssignMission.as_view(), name='assign-mission'),
    path('targets/<int:pk>/', views.TargetUpdate.as_view(), name='update-target'),
]
