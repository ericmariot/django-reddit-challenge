"""
Posts Models
"""
###
# Libraries
###
from django.db import models
from django.conf import settings
from django.utils.text import slugify

from helpers.models import TimestampModel

###
# Querysets
###


###
# Models
###
class Comment(TimestampModel):
    title = models.CharField(max_length=128)
    content = models.CharField(max_length=1024)
    upvotes = models.IntegerField(default=0)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="Comment",
    )
    post = models.ForeignKey(
        "posts.Post",
        on_delete=models.CASCADE,
        related_name="Comment",
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["upvotes"]
