from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Blog, BlogType
from django.db.models import Count
from read.utils import read_once_read


def get_blog_list_common_data(request, blogs_list):
    paginator = Paginator(blogs_list, 5)  # 博客列表分页 10
    page_num = request.GET.get('page', 1)  # 获取页码参数（GET请求）
    page_of_blogs = paginator.get_page(page_num)  # 得到具体页码参数的页面
    present_page_num = page_of_blogs.number  # 获取当前页面值
    page_range = list(range(max(present_page_num - 2, 1), present_page_num)) + \
                 list(range(present_page_num, min(present_page_num + 2, paginator.num_pages) + 1))
    # 加上省略页码标记
    if page_range[0] - 1 >= 2:
        page_range.insert(0, '...')
    if paginator.num_pages - page_range[-1] >= 2:
        page_range.append('...')

    # 加上首页和尾页。
    if page_range[0] != 1:
        page_range.insert(0, 1)
    if page_range[-1] != paginator.num_pages:
        page_range.append(paginator.num_pages)

    # 获取日期归档对应的博客数量
    blog_dates = Blog.objects.dates('created_time', 'month', order="DESC")
    blog_dates_dict = {}
    for blog_date in blog_dates:
        blog_count = Blog.objects.filter(created_time__year=blog_date.year,
                                         created_time__month=blog_date.month).count()
        blog_dates_dict[blog_date] = blog_count

    context = {}
    context['blogs'] = page_of_blogs.object_list
    context['page_of_blogs'] = page_of_blogs
    context['page_range'] = page_range
    context['blog_types'] = BlogType.objects.annotate(blog_count=Count('blog'))  # 文章分类
    context['blog_dates'] = blog_dates_dict

    return context


def blog_list(request):
    blogs_list = Blog.objects.all()  # 全部博客
    context = get_blog_list_common_data(request, blogs_list)
    return render(request, 'shop/blog_list.html', context)


def blog_with_type(request, blog_type_pk):
    blog_type = get_object_or_404(BlogType, pk=blog_type_pk)
    blogs_list = Blog.objects.filter(blog_type=blog_type)  # 筛选博客
    context = get_blog_list_common_data(request, blogs_list)
    context['blog_type'] = blog_type

    return render(request, 'shop/blog_with_type.html', context)


def blog_with_date(request, year, month):
    blogs_list = Blog.objects.filter(created_time__year=year, created_time__month=month)  # 全部博客
    context = get_blog_list_common_data(request, blogs_list)
    context['blog_with_date'] = '%s年%s月' % (year, month)

    return render(request, 'shop/blog_with_date.html', context)


def blog_detail(request, blog_pk):
    blog = get_object_or_404(Blog, pk=blog_pk)
    read_cookie_key = read_once_read(request, blog)

    context = {}
    context['previous_blog'] = Blog.objects.filter(created_time__gt=blog.created_time).last()
    context['next_blog'] = Blog.objects.filter(created_time__lt=blog.created_time).first()
    context['blog'] = blog
    response = render(request, 'shop/blog_detail.html', context)
    response.set_cookie(read_cookie_key, 'true')  # 阅读cookie的标记
    return response
