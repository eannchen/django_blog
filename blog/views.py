from django.shortcuts import render
from django.http import HttpResponse
from .models import Article, Category, Banner, Tag, Link
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def hello(request):
    return HttpResponse('歡迎使用Django！')


def global_variable(request):
    allcategory = Category.objects.all()
    remen = Article.objects.filter(tui__id=2)[:6]
    tags = Tag.objects.all()
    return locals()


# 首頁
def index(request):
    # 分類導覽
    # allcategory = Category.objects.all()
    # Banner
    banner = Banner.objects.filter(is_active=True)[0:4]
    # 推薦閱讀
    tui = Article.objects.filter(tui__id=1)[:3]
    # 最新文章
    allarticle = Article.objects.all().order_by('-id')[0:10]
    # 熱門文章排行
    hot = Article.objects.all().order_by('views')[:10]
    # 熱門推薦
    # remen = Article.objects.filter(tui__id=2)[:6]
    # 標籤
    # tags = Tag.objects.all()
    # 連結
    link = Link.objects.all()

    # context = {
    #     'allcategory': allcategory,
    #     'banner': banner,
    #     'tui': tui,
    #     'allarticle': allarticle,
    #     'hot': hot,
    #     'remen': remen,
    #     'tags': tags,
    #     'link': link,
    # }
    return render(request, 'index.html', locals())


def articles(request):
    allarticle = Article.objects.all()
    context = {
        'allarticle': allarticle,
    }
    return render(request, 'articles.html', context)


# 文章列表
def list(request, cid):
    list = Article.objects.filter(category_id=cid)
    # 當前文章種類
    cname = Category.objects.get(id=cid)
    # 推薦文章
    # remen = Article.objects.filter(tui__id=2)[:6]
    # 所有文章分類
    # allcategory = Category.objects.all()
    # 文章標籤
    # tags = Tag.objects.all()
    # 當前頁面
    page = request.GET.get('page')
    # 分頁
    paginator = Paginator(list, 5)

    try:
        # 當前頁碼的記錄
        list = paginator.page(page)
    except PageNotAnInteger:
        # 非整數頁時, 顯示第 1 頁的內容
        list = paginator.page(1)
    except EmptyPage:
        # 頁數不存在, 顯示最後一頁的內容
        list = paginator.page(paginator.num_pages)

    # locals() 返回一個當前作用域裡的所有變量及其值的字典
    return render(request, 'list.html', locals())


# 內容頁
def article(request, sid):
    # 指定文章
    show = Article.objects.get(id=sid)
    # 導航上的分類
    # allcategory = Category.objects.all()
    # 所有標籤
    # tags = Tag.objects.all()
    # 熱門推薦
    # remen = Article.objects.filter(tui__id=2)[:6]
    # 熱門文章
    hot = Article.objects.all().order_by('?')[:10]
    # 同分類上一篇
    previous_blog = Article.objects.filter(created_time__gt=show.created_time,
                                           category=show.category.id).first()
    # 同分類下一篇
    netx_blog = Article.objects.filter(created_time__lt=show.created_time,
                                       category=show.category.id).last()
    # 瀏覽次數 ++
    show.views = show.views + 1
    show.save()

    return render(request, 'article.html', locals())


# 標籤頁
def tag(request, tag):
    list = Article.objects.filter(tags__name=tag)
    # remen = Article.objects.filter(tui__id=2)[:6]
    # allcategory = Category.objects.all()
    tname = Tag.objects.get(name=tag)  #獲取當前搜索的標籤名
    page = request.GET.get('page')
    # tags = Tag.objects.all()
    paginator = Paginator(list, 5)
    try:
        list = paginator.page(page)
    except PageNotAnInteger:
        list = paginator.page(1)
    except EmptyPage:
        list = paginator.page(paginator.num_pages)
    return render(request, 'tags.html', locals())


# 搜索頁
def search(request):
    ss = request.GET.get('search')
    list = Article.objects.filter(title__icontains=ss)

    # remen = Article.objects.filter(tui__id=2)[:6]
    # allcategory = Category.objects.all()
    page = request.GET.get('page')
    # tags = Tag.objects.all()

    paginator = Paginator(list, 10)
    try:
        list = paginator.page(page)
    except PageNotAnInteger:
        list = paginator.page(1)
    except EmptyPage:
        list = paginator.page(paginator.num_pages)
    return render(request, 'search.html', locals())


# 關於我們
def about(request):
    allcategory = Category.objects.all()
    return render(request, 'about.html', locals())
