# Generated by Django 4.2.3 on 2023-07-18 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0006_remove_comments_user_comments_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='name',
            field=models.CharField(default='none', max_length=50),
        ),
        migrations.AlterField(
            model_name='comments',
            name='time_stamp',
            field=models.DateField(auto_now_add=True),
        ),
    ]
