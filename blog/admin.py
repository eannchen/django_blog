from django.contrib import admin
from .models import Banner, Category, Tag, Tui, Article, Link


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    # 文章列表想要顯示的字段
    list_display = ('id', 'category', 'title', 'tui', 'user', 'views',
                    'created_time')

    # 滿 50筆就自動分頁
    list_per_page = 50

    # 列表排序方式
    ordering = ('-created_time', )

    # 設置哪些字段可以點擊進入編輯界面
    list_display_links = ('id', 'title')


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'text_info', 'img', 'link_url', 'is_active')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'index')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Tui)
class TuiAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'linkurl')
