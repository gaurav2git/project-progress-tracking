from django.contrib.auth.views import LoginView

from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('register/', views.register, name="register"),
    path('profile/', views.profile, name="profile"),
]