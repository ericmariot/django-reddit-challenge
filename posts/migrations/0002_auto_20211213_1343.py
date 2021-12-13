# Generated by Django 3.2.6 on 2021-12-13 13:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("posts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="author",
            field=models.ForeignKey(
                default=0,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="post",
                to="accounts.user",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="post",
            name="upvotes",
            field=models.IntegerField(default=0),
        ),
    ]