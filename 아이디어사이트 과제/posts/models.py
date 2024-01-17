from django.db import models

class IdeaItem(models.Model):
    title = models.CharField('아이디어명',max_length=30)
    photo = models.ImageField('이미지', blank=True, upload_to='posts/%Y%m%d')
    content = models.TextField('아이디어 설명', max_length=300)
    like = models.IntegerField('아이디어 관심도', default=0)

    def __str__(self):
        return self.title
