# Generated by Django 5.0.2 on 2024-02-13 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_keyword_remove_post_keywords_post_keywords'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='keywords',
            field=models.ManyToManyField(null=True, to='blog.keyword'),
        ),
    ]
