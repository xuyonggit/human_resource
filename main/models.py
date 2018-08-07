from django.db import models


# Create your models here.
class notes(models.Model):
    id = models.AutoField(primary_key=True)     # ID
    name = models.CharField(max_length=255, default=None)   # 姓名
    from_user = models.CharField(max_length=255, default=None)      # 推荐人
    notes = models.CharField(max_length=255, default=None)          # 简历链接
