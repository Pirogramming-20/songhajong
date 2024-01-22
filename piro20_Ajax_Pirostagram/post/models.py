from django.db import models
from user.models import User

class Post(models.Model):
    post_user = models.ForeignKey(User, on_delete = models.CASCADE, null=True, blank=True, related_name='post_user')
    title = models.CharField('제목',max_length=30)
    photo = models.ImageField('이미지', blank=True, upload_to='posts/%Y%m%d')
    content = models.TextField('내용', max_length=300)
    like = models.IntegerField('좋아요', default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content