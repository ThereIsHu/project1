# Generated by Django 4.2.5 on 2023-09-08 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="admin",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=20, verbose_name="管理员账号")),
                ("password", models.CharField(max_length=20, verbose_name="管理员密码")),
            ],
        ),
        migrations.CreateModel(
            name="answer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("key", models.CharField(max_length=20, verbose_name="关键字")),
                ("text", models.CharField(max_length=20, verbose_name="文本")),
                ("picture", models.CharField(max_length=20, verbose_name="图片")),
                ("url", models.CharField(max_length=20, verbose_name="链接")),
            ],
        ),
        migrations.CreateModel(
            name="login",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("ip", models.CharField(max_length=20, verbose_name="ip地址")),
                ("browserType", models.CharField(max_length=20, verbose_name="浏览器类型")),
            ],
        ),
        migrations.CreateModel(
            name="words",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("word", models.CharField(max_length=1000, verbose_name="词频")),
                ("times", models.TimeField(verbose_name="时间")),
            ],
        ),
        migrations.RemoveField(model_name="user", name="age",),
        migrations.AddField(
            model_name="user",
            name="password",
            field=models.CharField(default=200, max_length=20, verbose_name="用户密码"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="user",
            name="name",
            field=models.CharField(max_length=20, verbose_name="用户账号"),
        ),
    ]
