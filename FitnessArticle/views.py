from django.shortcuts import render, get_object_or_404
from .models import ArticleCategory, Tag, Recommend, Article, Slide, Link, MuscleCategory, MuscleTag, Muscle, \
                     DietPlanCategory, DietPlan, Plan, Food, FoodCategory
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger  # 导入django自带的分页功能插件


# 此函数返回article的首页home
def home(request):
    all_category = ArticleCategory.objects.all()  # 对ArticleCategory进行声明并实例化，all_category, 文章分类
    slides = Slide.objects.filter(is_active=True)[0:4]  # 查询幻灯片的数据， 进行切片
    recommend = Article.objects.filter(recommend__id=2)[:3]  # 推荐id=2的健身入门必读
    all_article = Article.objects.all().order_by('-id')[:10]  # -id 筛选数据排序方式 逆序，索引前十
    hot_articles = Article.objects.all().order_by('reading')[:10]  # 热门文章按照阅读数reading 进行排序 读取十篇
    hot_recommends = Article.objects.filter(recommend__id=2)[:6]  # 热门推荐 id=2的健身入门文章前六篇文章
    tags = Tag.objects.all()
    links = Link.objects.all()

    # 把查询的对象封装到上下文
    content = {
        'all_category': all_category,
        'slides': slides,
        'recommend': recommend,
        'all_article': all_article,
        'hot_articles': hot_articles,
        'hot_recommends': hot_recommends,
        'tags': tags,
        'links': links,
    }
    # 把数据传到模板页面
    return render(request, 'FitnessArticle/home.html', content)


def article_list(request, lid):  # 文章列表页
    article_lists = Article.objects.filter(category_id=lid)  # 获取通过URL传进来的lid，然后筛选对应的文章
    acname = ArticleCategory.objects.get(id=lid)  # 获取当前文章类别的名字
    hot_recommends = Article.objects.filter(recommend__id=2)[:6]  # 热门推荐 id=2的健身入门文章前六篇文章
    all_category = ArticleCategory.objects.all()  # 对ArticleCategory进行声明并实例化，all_category, 文章分类
    tags = Tag.objects.all()  # home页面 右侧的文章标签
    # 分页功能的实现
    page = request.GET.get('page')  # 在URl中获取当前的页面
    paginator = Paginator(article_lists, 5)  # 对查询的数据进行分页 5
    try:
        lists = paginator.page(page)  # 获取当前的页码记录
    except PageNotAnInteger:
        lists = paginator.page(1)  # 如果用户输入的页码不是整数，显示第一页
    except EmptyPage:
        lists = paginator.page(paginator.num_pages)  # 如果用户输入的页码不在系统 显示最后一页内容

    # locals()替代content{...} 返回一个包含当前作用域里面的所有的变量和它们的值的字典
    return render(request, 'FitnessArticle/article_list.html', locals())


def article_show(request, sid):  # 文章内容页
    article_shows = Article.objects.get(id=sid)  # 查询指定的ID文章
    all_category = ArticleCategory.objects.all()  # 对ArticleCategory进行声明并实例化，all_category, 文章分类
    tags = Tag.objects.all()  # home页面 右侧的文章标签
    hot_recommends = Article.objects.filter(recommend__id=2)[:6]  # 热门推荐 id=2的健身入门文章前六篇文章
    hot_articles = Article.objects.all().order_by('?')[:10]  # 下面感兴趣的文章，随机推荐
    previous_article = Article.objects.filter(created_time__gt=article_shows.created_time,
                                              category=article_shows.category.id).first()  # 上一篇文章
    next_article = Article.objects.filter(created_time__lt=article_shows.created_time,
                                          category=article_shows.category.id).last()  # 下篇一文章
    article_shows.reading = article_shows.reading + 1
    article_shows.save()  # 阅读数+1
    return render(request, 'FitnessArticle/article_show.html', locals())


def tag(request, tag):  # 文章标签页
    tag_articles = Article.objects.filter(tags__name=tag)  # 通过文章标签进行查询
    hot_recommends = Article.objects.filter(recommend__id=2)[:6]
    all_category = ArticleCategory.objects.all()  # 对ArticleCategory进行声明并实例化，all_category, 文章分类
    tname = Tag.objects.get(name=tag)  # 获取当前搜索的标签名
    # 分页功能的实现
    page = request.GET.get('page')  # 在URl中获取当前的页面
    tags = Tag.objects.all()
    paginator = Paginator(tag_articles, 5)  # 对查询的数据进行分页 5
    try:
        lists = paginator.page(page)  # 获取当前的页码记录
    except PageNotAnInteger:
        lists = paginator.page(1)  # 如果用户输入的页码不是整数，显示第一页
    except EmptyPage:
        lists = paginator.page(paginator.num_pages)  # 如果用户输入的页码不在系统 显示最后一页内容

    # locals()替代content{...} 返回一个包含当前作用域里面的所有的变量和它们的值的字典
    return render(request, 'FitnessArticle/tags.html', locals())


def muscle_home(request):  # 肌肉主页
    all_muscle_category = MuscleCategory.objects.all()  # 对MuscleCategory进行声明并实例化，all_muscle_category, 肌肉分类
    slides = Slide.objects.filter(is_active=True)[4:6]  # 查询幻灯片的数据， 进行切片
    muscle = Muscle.objects.all()
    muscle_tags = MuscleTag.objects.all()
    return render(request, 'Muscle/muscle_home.html', locals())


def muscle_show(request, sid):  # 肌肉内容显示
    muscle_shows = Muscle.objects.get(id=sid)
    all_muscle_category = MuscleCategory.objects.all()
    other_muscles = Muscle.objects.all().order_by('?')[0:7]
    muscle_tags = MuscleTag.objects.all().order_by('id')
    return render(request, 'Muscle/muscle_show.html', locals())


def plan_home(request):
    plans = Plan.objects.all()
    return render(request, 'Plan/plan_home.html', locals())


def food(request):
    food_category = FoodCategory.objects.all()
    diet_plan_category = DietPlanCategory.objects.all()
    return render(request, 'Food/food.html', locals())


def food_list(request, lid):
    foods_list = Food.objects.filter(category_id=lid)
    acname = FoodCategory.objects.get(id=lid)  # 获取当前文章类别的名字
    # 分页功能的实现
    """
    a_page = request.GET.get('page')  # 在URl中获取当前的页面
    paginator = Paginator(foods_list, 5)  # 对查询的数据进行分页 5
    try:
        lists = paginator.page(a_page)  # 获取当前的页码记录
    except PageNotAnInteger:
        lists = paginator.page(1)  # 如果用户输入的页码不是整数，显示第一页
    except EmptyPage:
        lists = paginator.page(paginator.num_pages)  # 如果用户输入的页码不在系统 显示最后一页内容
    """
    return render(request, 'Food/food_list.html', locals())




def diet_plan_list(request, lid):
    all_plan_list = DietPlan.objects.filter(category_id=lid)
    acname = DietPlanCategory.objects.get(id=lid)  # 获取当前文章类别的名字

    return render(request, 'Food/diet_plan_list.html', locals())


def diet_plan(request, sid):
    diet = get_object_or_404(DietPlan, pk=sid)  # 获取pk文章
    return render(request, 'Food/diet_plan.html', locals())  # 返回article_detail.html页面

