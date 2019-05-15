from django.db import models
from django.contrib.auth.models import User
from DjangoUeditor.models import UEditorField


# 文章分類
class Category(models.Model):
    name = models.CharField('分類', max_length=100)
    index = models.IntegerField(default=999, verbose_name='分類排序')

    class Meta:
        verbose_name = '分類'
        # If this isn't given, Django will use verbose_name + "s".
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 文章標籤
class Tag(models.Model):
    name = models.CharField('文章標籤', max_length=100)

    class Meta:
        verbose_name = '文章標籤'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 推薦位
class Tui(models.Model):
    name = models.CharField('推薦位', max_length=100)

    class Meta:
        verbose_name = '推薦位'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 文章
class Article(models.Model):
    title = models.CharField('標題', max_length=70)
    excerpt = models.TextField('摘要', max_length=200, blank=True)  # blank 允許空白

    # 使用外鍵關聯分類表與分類是一對多關係
    category = models.ForeignKey(
        Category,
        on_delete=models.DO_NOTHING,  # 關聯被刪除時,什麼也不做
        verbose_name='分類',
        blank=True,
        null=True)

    # 使用外鍵關聯標籤表與標籤是多對多關係
    tags = models.ManyToManyField(Tag, verbose_name='標籤', blank=True)

    img = models.ImageField(
        upload_to=
        'article_img/%Y/%m/%d/',  # file will be saved to MEDIA_ROOT/article_img/2015/01/30
        verbose_name='文章圖片',
        blank=True,
        null=True)

    # body = models.TextField()
    # 需將 lib\site-packages\django\forms\boundfield.py 第 93 行註解才不會報錯
    body = UEditorField('內容',
                        width=800,
                        height=500,
                        toolbars="full",
                        imagePath="upimg/",
                        filePath="upfile/",
                        upload_settings={"imageMaxSize": 1204000},
                        settings={},
                        command=None,
                        blank=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,  # 關聯被刪除時,資料也刪除
        verbose_name='作者')

    views = models.PositiveIntegerField('瀏覽次數', default=0)
    tui = models.ForeignKey(Tui,
                            on_delete=models.DO_NOTHING,
                            verbose_name='推薦位',
                            blank=True,
                            null=True)

    created_time = models.DateTimeField(
        '發佈時間',
        auto_now_add=True  # 初建時自動寫入時間，再設定時會被略過
    )
    modified_time = models.DateTimeField('修改時間', auto_now=True)

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章'

    def __str__(self):
        return self.title


# Banner
class Banner(models.Model):
    text_info = models.CharField('標題', max_length=50, default='')
    img = models.ImageField('輪播圖', upload_to='banner/')
    link_url = models.URLField('圖片鏈接', max_length=100)
    is_active = models.BooleanField('是否是active', default=False)

    def __str__(self):
        return self.text_info

    class Meta:
        verbose_name = '輪播圖'
        verbose_name_plural = '輪播圖'


# 友站連結
class Link(models.Model):
    name = models.CharField('連結名稱', max_length=20)
    linkurl = models.URLField('網址', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '友站連結'
        verbose_name_plural = '友站連結'