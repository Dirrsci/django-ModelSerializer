from django.urls import path
from sc import views

urlpatterns = [
    path('users/', views.user_list),
    path('users/<int:pk>/', views.user_details),
    path('users/<int:pk>/groups', views.user_groups),
]