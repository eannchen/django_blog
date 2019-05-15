"""django_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from blog import views
from django.views.static import serve
from django_blog import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),  # 首頁
    path('list-<int:cid>.html', views.list, name='list'),  # 列表頁
    path('show-<int:sid>.html', views.article, name='show'),  # 內容頁
    path('tag/<tag>', views.tag, name='tags'),  # 標籤列頁
    path('s/', views.search, name='search'),  # 搜索列表頁
    path('about/', views.about, name='about'),  # 聯繫我們單頁
    path('ueditor/', include('DjangoUeditor.urls')),
    re_path('^media/(?P<path>.*)$', serve,
            {'document_root': settings.MEDIA_ROOT}),
]
