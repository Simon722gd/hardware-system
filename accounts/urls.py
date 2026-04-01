from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.custom_login, name='login'),
    path('logout/', views.custom_logout, name='logout'),
    path('forgot-password/', views.forgot_password_step1, name='forgot_password_step1'),
    path('reset-password/', views.forgot_password_step2, name='forgot_password_step2'),
]
