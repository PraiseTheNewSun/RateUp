# Generated by Django 4.2.11 on 2024-11-20 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rating', '0002_rename_comments_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_author',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='post_date_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
