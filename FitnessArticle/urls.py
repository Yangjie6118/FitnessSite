from django.urls import path
from . import views


app_name = 'FitnessArticle'
urlpatterns = [
    path('', views.home, name='home'),  # 健身文章主页
    path('list-<int:lid>.html/', views.article_list, name='article_list'),  # 列表页
    path('show-<int:sid>.html/', views.article_show, name='article_show'),  # 内容页
    path('tag/<tag>/', views.tag, name='tag'),  # 标签列表页
    path('muscle/', views.muscle_home, name='muscle_home'),  # 肌肉模块主页
    path('muscle_show-<int:sid>.html/', views.muscle_show, name='muscle_show'),  # 肌肉内容页
    path('plan/', views.plan_home, name='plan_home'),  # 训练计划主页
    path('food/', views.food, name='food'),  # 健身饮食主页
    path('food_list-<int:lid>.html/', views.food_list, name='food_list'),
    path('diet_plan_list-<int:lid>.html/', views.diet_plan_list, name='diet_plan_list'),
    path('diet_plan-<int:sid>.html/', views.diet_plan, name='diet_plan'),
]

