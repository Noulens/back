# Generated by Django 5.0.2 on 2024-02-13 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_post_keywords'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='keywords',
        ),
        migrations.DeleteModel(
            name='Keyword',
        ),
        migrations.AddField(
            model_name='post',
            name='keywords',
            field=models.TextField(null=True),
        ),
    ]
