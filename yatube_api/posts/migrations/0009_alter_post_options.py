# Generated by Django 3.2.16 on 2023-05-14 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_remove_follow_unique_subscription'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['pub_date'], 'verbose_name': 'Пост', 'verbose_name_plural': 'Посты'},
        ),
    ]