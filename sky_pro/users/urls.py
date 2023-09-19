from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    # URL для входа (авторизации)
    path('login/', views.login_view, name='login'),

    # URL для выхода (логаута)
    path('logout/', views.logout_view, name='logout'),

    # URL для регистрации (если используется предыдущий код)
    path('register/', views.register, name='register'),
]
