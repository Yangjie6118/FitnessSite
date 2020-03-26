from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from ckeditor_uploader.fields import RichTextUploadingField
from read.models import ReadNumExpandMethod


# 第一步
class BlogType(models.Model):
    name = models.CharField(max_length=15, verbose_name="博客分类名")

    class Meta:
        verbose_name = '文章类别'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Blog(models.Model, ReadNumExpandMethod):
    title = models.CharField(max_length=30,  verbose_name='标题')  # 创建文章的标题
    blog_type = models.ForeignKey(BlogType, on_delete=models.CASCADE, verbose_name='分类') #blog_type关联到上面的BlogType
    content = RichTextUploadingField()  # 创建文章的内容
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # 创建作者，一个作者对应多篇文章

    created_time = models.DateTimeField(auto_now_add=True)    # 刚开始创建的时间不变
    change_time = models.DateTimeField(auto_now=True)  #后面更改的时间日期要变化

    def get_url(self):
        return reverse('shop:blog_detail', kwargs={'blog_pk': self.pk})

    def get_email(self):
        return self.author.email

    def __str__(self):
        return self.title  # 在后台显示出 文章的标题

    class Meta:
        verbose_name = '个人博客'
        verbose_name_plural = verbose_name
        ordering = ['-created_time']

