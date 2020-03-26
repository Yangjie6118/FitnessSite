from django.urls import path, include
from . import views

urlpatterns = [
    path('login_for_medal/', views.login_for_medal, name='login_for_medal'),  # 模态登录框 位于blog_detail
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('user_info/', views.user_info, name='user_info'),
    path('chang_nickname/', views.chang_nickname, name='chang_nickname'),
    path('bind_email/', views.bind_email, name='bind_email'),
    path('send_verification_code/', views.send_verification_code, name='send_verification_code'),
    path('change_password/', views.change_password, name='change_password'),
    path('forgot_password/', views.forgot_password, name='forgot_password'),
]