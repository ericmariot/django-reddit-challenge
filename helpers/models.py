"""
Model helper
"""
###
# Libraries
###
from django.db import models
from django.utils.translation import ugettext as _

###
# Helpers
###
class TimestampModel(models.Model):
    '''
        Extend this model if you wish to have automatically updated
        created_at and updated_at fields.
    '''

    class Meta:
        abstract = True

    created_at = models.DateTimeField(null=False, blank=True, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, blank=True, auto_now=True)


class UpvoteDownvoteModel(models.Model):
    class Vote(models.TextChoices):
        UPVOTED = "upvoted", _("Upvoted")
        DOWNVOTED = "downvoted", ("Downvoted")

    class Meta:
        abstract = True

    vote = models.CharField(choices=Vote.choices, max_length=10, blank=True)