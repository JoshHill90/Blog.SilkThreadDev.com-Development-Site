# Generated by Django 4.2.3 on 2023-07-22 22:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_profile_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='icon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='members.usericon'),
        ),
        migrations.AlterField(
            model_name='usericon',
            name='icon',
            field=models.URLField(blank=True),
        ),
    ]
