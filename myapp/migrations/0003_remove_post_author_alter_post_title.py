# Generated by Django 5.0.4 on 2024-05-08 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0002_post"),
    ]

    operations = [
        migrations.RemoveField(model_name="post", name="author",),
        migrations.AlterField(
            model_name="post",
            name="title",
            field=models.CharField(max_length=200, verbose_name="작성자"),
        ),
    ]