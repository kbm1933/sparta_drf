'''
모델정의:
-모델을 생성할때 들어가야할 초기화(?) 변수들 예를 들어 게시글 모델을 만든다고 하면
title(제목),
content(내용),
create(생성 시간),
update(수정 시간)

'''
from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length = 256)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)