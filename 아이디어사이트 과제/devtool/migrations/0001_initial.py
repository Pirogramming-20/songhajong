# Generated by Django 5.0.1 on 2024-01-17 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='devTool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='이름')),
                ('kind', models.CharField(max_length=30, verbose_name='종류')),
                ('content', models.TextField(max_length=300, verbose_name='개발툴 설명')),
            ],
        ),
    ]
