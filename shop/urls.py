from django.urls import path
from . import views

app_name = 'shop'
urlpatterns = [
    path('', views.blog_list, name='blog_list'),  # 定义个人纪录主页列表
    path('detail/<int:blog_pk>/', views.blog_detail, name='blog_detail'),
    path('type/<int:blog_type_pk>/', views.blog_with_type, name='blog_with_type'),
    path('date/<int:year>/<int:month>/', views.blog_with_date, name='blog_with_date'),
]
