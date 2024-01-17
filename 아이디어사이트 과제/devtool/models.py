from django.db import models

class devTool(models.Model):
    name= models.CharField('이름',max_length=30)
    kind = models.CharField('종류', max_length=30)
    content = models.TextField('개발툴 설명', max_length=300)

    def __str__(self):
        return self.name
