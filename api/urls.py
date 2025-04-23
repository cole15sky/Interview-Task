from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView
from .views import signup, login, profile, logout, TaskListCreateView, TaskDetailView



urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('profile/', views.profile, name='profile'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), 
    path('logout/', views.logout, name='logout'),
    
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),


]