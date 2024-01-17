# Generated by Django 5.0.1 on 2024-01-16 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IdeaItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='아이디어명')),
                ('photo', models.ImageField(blank=True, upload_to='posts/%Y%m%d', verbose_name='이미지')),
                ('content', models.TextField(max_length=300, verbose_name='아이디어 설명')),
                ('like', models.IntegerField(default=0, verbose_name='아이디어 관심도')),
            ],
        ),
    ]
