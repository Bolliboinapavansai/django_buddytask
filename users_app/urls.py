from django.urls import path
from users_app.views import registration
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register', registration, name='registration'),
    path('login',auth_views.LoginView.as_view(template_name='login.html'), name='login' ),
    path('logout', auth_views.LogoutView.as_view(next_page='/'), name='logout')
]