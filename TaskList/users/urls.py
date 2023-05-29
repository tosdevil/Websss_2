from django.urls import path
from . import views
from .views import CustomLoginView, RegisterPage

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('logout/', LogoutView.as_view(next_page = 'tasks_home'), name = 'logout'),
    path('', RegisterPage.as_view(), name = 'register'),
    path('login/', CustomLoginView.as_view(), name = 'login')
]