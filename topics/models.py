"""
Topics Models
"""
###
# Libraries
###
from django.db import models
from django.conf import settings
from django.utils.translation import ugettext as _

from helpers.models import TimestampModel

###
# Querysets
###


###
# Models
###
class Topic(TimestampModel):
    name = models.CharField(max_length=128)
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=256)
    url_name = models.SlugField(max_length=64) # should I use unique=True?
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="topic",
    )

    def __str__(self):
        return self.title
