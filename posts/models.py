"""
Posts Models
"""
###
# Libraries
###
from django.db import models
from django.conf import settings
from django.db.models import Q, Count

from helpers.models import TimestampModel, UpvoteDownvoteModel

###
# Querysets
###


###
# Models
###
class PostVotesManager(models.Manager):
    def with_votes(self):
        return self.annotate(
            total_upvotes=Count("vote", filter=Q(vote=Post.Vote.UPVOTED))
        )


class Post(TimestampModel, UpvoteDownvoteModel):
    objects = PostVotesManager()

    title = models.CharField(max_length=128)
    content = models.CharField(max_length=1024)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="post",
    )
    topic = models.ForeignKey(
        "topics.Topic",
        on_delete=models.CASCADE,
        related_name="post",
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-updated_at"]
