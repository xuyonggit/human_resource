from django.db import models
from datetime import datetime, date


# Create your models here.
class notes(models.Model):
    id = models.AutoField(primary_key=True)     # ID
    name = models.CharField(max_length=255, default=None)   # 姓名
    from_user = models.CharField(max_length=255, default=None)      # 推荐人
    notes = models.CharField(max_length=255, default=None)          # 简历链接
    position = models.CharField(max_length=255, default=None)       # 职位
    position_level = models.CharField(max_length=255, default=None)       # 级别
    base_num = models.IntegerField('基数', default=0)             # 奖励基数
    create_date = models.DateField(auto_now_add=True)                   # 创建日期，默认now
    modify_date = models.DateField(auto_now=True)                   # 最新修改日期，默认now
    status = models.CharField(max_length=20, default="提交简历")    # 状态


class tb_from_user(models.Model):
    id = models.AutoField(primary_key=True)     # ID
    username = models.CharField('用户名', max_length=255, default=None)   # 用户名
    recommend_count = models.IntegerField('已推荐人数', default=0)   # 已推荐数量
    reputation = models.IntegerField('信誉分数', default=100,)   # 信誉分数


class base_template(models.Model):
    id = models.AutoField(primary_key=True)     # ID
    position_level = models.CharField(max_length=255, default=None)     # 级别
    base_num = models.IntegerField('基数', default=0)     # 奖励基数

