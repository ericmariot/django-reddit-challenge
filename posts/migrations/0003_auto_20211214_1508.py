# Generated by Django 3.2.6 on 2021-12-14 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0002_auto_20211213_1343"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="post",
            options={"ordering": ["-updated_at"]},
        ),
        migrations.RemoveField(
            model_name="post",
            name="upvotes",
        ),
        migrations.AddField(
            model_name="post",
            name="vote",
            field=models.CharField(
                blank=True,
                choices=[("upvoted", "Upvoted"), ("downvoted", "Downvoted")],
                max_length=10,
            ),
        ),
    ]
