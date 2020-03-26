from django.contrib import admin
from .models import Blog, BlogType
# Register your models here.

# 注册文章分类列表
@admin.register(BlogType)
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


# 注册文章分类列表
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content', 'author', 'created_time']
    # 满20条数据就自动分页
    list_per_page = 10
    # 后台数据列表排序方式
    ordering = ('-created_time',)
    list_display_links = ('id', 'title')