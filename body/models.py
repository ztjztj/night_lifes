from django.db import models

class BodyUser(models.Model):
    userNumber = models.CharField(max_length=20,verbose_name="账号")
    password = models.CharField(max_length=20, verbose_name="密码")
    user_name = models.CharField(max_length=20, verbose_name="用户名")

    class Meta:
        managed = False
        db_table = 'body_user'

class BodyNoval(models.Model):

    book_name = models.CharField(max_length=20, verbose_name="书名")
    book_img = models.TextField(verbose_name="书籍图片URL")
    book_author = models.CharField(max_length=20, verbose_name="作者")
    book_category = models.CharField(max_length=20, verbose_name="类别")
    book_state = models.CharField(max_length=20, verbose_name="状态")
    book_update = models.DateTimeField(verbose_name='最后更新时间')
    book_intro = models.TextField(verbose_name='简介')
    book_xiao = models.IntegerField(verbose_name='书籍销量')
    book_url = models.TextField(verbose_name='图书URL')
    book_gex = models.CharField(max_length=10,verbose_name='男女分类')

    class Meta:
        managed = False
        db_table = 'body_noval'


# 小说详细内容
class Noval_room(models.Model):

    book_section = models.CharField(max_length=200, verbose_name="每一章节")
    book_content = models.TextField(verbose_name="章节内容")
    book_foreign = models.TextField(verbose_name="书籍url")
    book_chapter_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'body_noval_room'

# 书架
class bookrack(models.Model):
    book_add = models.DateField(auto_now_add=True, verbose_name="添加时间")
    user_foregin = models.ForeignKey(to=BodyUser, on_delete=models.CASCADE, verbose_name="用户id")
    Noval_foregin = models.ForeignKey(to=BodyNoval, on_delete=models.CASCADE, verbose_name="书籍id")

    class Meta:
        managed = False
        db_table = 'body_bookrack'


# 章节
class ChapterUrls(models.Model):
    chapter_id = models.TextField(blank=True, null=True)
    chapter_url = models.TextField(blank=True, null=True)
    chapter_name = models.TextField(blank=True, null=True)
    book_url = models.TextField(blank=True, null=True)
    is_use = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chapter_urls'
