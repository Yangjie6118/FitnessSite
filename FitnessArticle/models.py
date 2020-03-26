from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField


# 导入django自带的用户模块

# 文章分类
class ArticleCategory(models.Model):
    name = models.CharField(max_length=50, verbose_name="文章分类名")
    index = models.IntegerField(default=0, verbose_name='分类排序')
    
    class Meta:
        verbose_name = '文章类别'
        verbose_name_plural = verbose_name
    
    def __str__(self):
        return self.name

    
# 文章标签
class Tag(models.Model):
    name = models.CharField(max_length=50, verbose_name='文章标签')
    
    class Meta:
        verbose_name = '文章标签'
        verbose_name_plural = verbose_name
        
    def __str__(self):
        return self.name


# 热门推荐
class Recommend(models.Model):
    name = models.CharField(max_length=50, verbose_name='推荐位置')
    
    class Meta:
        verbose_name = '推荐位'
        verbose_name_plural = verbose_name
    
    def __str__(self):
        return self.name
    
    
# 文章
class Article(models.Model):
    title = models.CharField(max_length=50, verbose_name='标题')
    category = models.ForeignKey(ArticleCategory, on_delete=models.DO_NOTHING, verbose_name='分类')
    tags = models.ManyToManyField(Tag, verbose_name='标签')
    picture = models.ImageField(upload_to='Article_img/%Y/%m/%d/', blank=True, verbose_name='文章图片')
    content = RichTextUploadingField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者')
    '''
    文章作者，这里的User是从django.contrib.auth.models导入的
    '''
    reading = models.PositiveIntegerField(default=0, verbose_name='阅读量')  # 正整数字段
    recommend = models.ForeignKey(Recommend, on_delete=models.DO_NOTHING, verbose_name='热门推荐')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    change_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


# 幻灯片Slide
class Slide(models.Model):
    text_info = models.CharField(max_length=50, default='', verbose_name='图片标题')
    img = models.ImageField(upload_to='Slide_img', verbose_name='幻灯图片')
    link_url = models.URLField(max_length=100, verbose_name='图片链接')
    is_active = models.BooleanField(default=False, verbose_name='是否动态')

    class Meta:
        verbose_name = '幻灯片'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.text_info


# 友情链接
class Link(models.Model):
    name = models.CharField(max_length=20, verbose_name='链接名称')
    link_url = models.URLField(max_length=100, verbose_name='网址')

    class Meta:
        verbose_name = '友情链接'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 肌肉部位分类
class MuscleCategory(models.Model):
    name = models.CharField(max_length=50, verbose_name="肌肉部位名")
    index = models.IntegerField(default=0, verbose_name='分类排序')

    class Meta:
        verbose_name = '肌肉部位分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 肌肉标签
class MuscleTag(models.Model):
    name = models.CharField(max_length=50, verbose_name='肌肉标签')

    class Meta:
        verbose_name = '肌肉标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 肌肉模块
class Muscle(models.Model):
    title = models.CharField(max_length=50, verbose_name='肌肉模块标题')
    category = models.ForeignKey(MuscleCategory, on_delete=models.DO_NOTHING, verbose_name='肌肉分类')
    tags = models.ManyToManyField(MuscleTag, verbose_name='肌肉标签')
    picture = models.ImageField(upload_to='Muscle_img', blank=True, verbose_name='肌肉图片')
    content = RichTextUploadingField()
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    change_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')

    class Meta:
        verbose_name = '肌肉'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


# 训练计划模块
class Plan(models.Model):
    title = models.CharField(max_length=50, verbose_name='训练计划模块标题')
    abstract = models.CharField(max_length=100, verbose_name='文章摘要')
    tags = models.ManyToManyField(MuscleTag, verbose_name='肌肉标签')
    picture = models.ImageField(upload_to='Plan_img', blank=True, verbose_name='训练计划图片')
    content = RichTextUploadingField()
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    change_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')

    class Meta:
        verbose_name = '训练计划'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


# 食物分类
class FoodCategory(models.Model):
    name = models.CharField(max_length=50, verbose_name='食物类别')
    picture = models.ImageField(upload_to='FoodCategory_img', blank=True, verbose_name='食物类图片')
    txt_info = models.CharField(max_length=50, default='', verbose_name='食物简介')
    index = models.IntegerField(default=0, verbose_name='分类排序')

    class Meta:
        verbose_name = '食物分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 食物
class Food(models.Model):
    title = models.CharField(max_length=50, verbose_name='食物名')
    category = models.ForeignKey(FoodCategory, on_delete=models.DO_NOTHING, verbose_name='食物类别')
    picture = models.ImageField(upload_to='Food_img', blank=True, verbose_name='食物图片')
    content = RichTextUploadingField()
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    change_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')

    class Meta:
        verbose_name = '食物'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


# 饮食计划分类
class DietPlanCategory(models.Model):
    name = models.CharField(max_length=50, verbose_name='饮食计划分类名')
    index = models.IntegerField(default=0, verbose_name='分类排序')

    class Meta:
        verbose_name = '饮食计划分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 饮食计划
class DietPlan(models.Model):
    title = models.CharField(max_length=50, verbose_name='饮食计划标题')
    category = models.ForeignKey(DietPlanCategory, on_delete=models.DO_NOTHING, verbose_name='分类')
    picture = models.ImageField(upload_to='DietPlan_img', blank=True, verbose_name='饮食计划图片')
    content = RichTextUploadingField()
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    change_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')

    class Meta:
        verbose_name = '饮食计划'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


