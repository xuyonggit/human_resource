from django.db import models


# Create your models here.
class notes(models.Model):
    id = models.AutoField(primary_key=True)     # ID
    name = models.CharField(max_length=255, default=None)   # 姓名
    from_user = models.CharField(max_length=255, default=None)      # 推荐人
    notes = models.CharField(max_length=255, default=None)          # 简历链接


class tb_from_user(models.Model):
    id = models.AutoField(primary_key=True)     # ID
    username = models.CharField('用户名', max_length=255, default=None)   # 用户名
    recommend_count = models.IntegerField('已推荐人数', default=0)   # 已推荐数量
    reputation = models.IntegerField('信誉分数', default=100,)   # 信誉分数
