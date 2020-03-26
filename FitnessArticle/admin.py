from django.contrib import admin
from .models import ArticleCategory, Tag, Recommend, Article, Slide, Link, MuscleCategory, MuscleTag, Muscle, \
    Plan, Food, FoodCategory, DietPlanCategory, DietPlan

# Register your models here.

# 注册文章列表
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    # 文章列表显示的字段
    list_display = ['id', 'category', 'title', 'recommend', 'reading', 'author', 'created_time']
    # 满20条数据就自动分页
    list_per_page = 20
    # 后台数据列表排序方式
    ordering = ('-created_time',)
    # 设置哪些字段可以点击进入编辑界面
    list_display_links = ('id', 'title')


# 注册文章分类列表
@admin.register(ArticleCategory)
class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'index']


# 注册标签列表
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


# 注册推荐列表
@admin.register(Recommend)
class RecommendAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


# 注册首页幻灯片列表
@admin.register(Slide)
class SlideAdmin(admin.ModelAdmin):
    list_display = ['id', 'text_info', 'img', 'link_url', 'is_active']


# 注册友情链接
@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'link_url']


# 注册肌肉部位分类
@admin.register(MuscleCategory)
class MuscleCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'index']


# 注册肌肉标签
@admin.register(MuscleTag)
class MuscleTagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


# 注册肌肉模块
@admin.register(Muscle)
class MuscleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'created_time']
    # 设置哪些字段可以点击进入编辑界面
    list_display_links = ('id', 'title')


# 注册训练计划模块
@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'abstract', 'created_time']
    list_display_links = ('id', 'title')


# 注册食物模块
@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'created_time']
    # 满20条数据就自动分页
    list_per_page = 20
    # 后台数据列表排序方式
    ordering = ('-created_time',)
    list_display_links = ('id', 'title')


# 注册食物类别
@admin.register(FoodCategory)
class FoodCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'txt_info', 'index']

# 注册饮食计划类别
@admin.register(DietPlanCategory)
class DietPlanCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'index']


# 注册饮食计划
@admin.register(DietPlan)
class DietPlanAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'created_time']
    list_display_links = ('id', 'title')



