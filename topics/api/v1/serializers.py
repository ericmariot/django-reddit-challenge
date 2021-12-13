"""
API V1: Topics Serializers
"""

###
# Libraries
###
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from accounts.api.v1.serializers import UserModelUsernameSerializer
from posts.models import Post
from posts.api.v1.serializers import (
    NestedPostSerializer,
)
from topics.models import Topic

###
# Serializers
class TopicSerializer(serializers.ModelSerializer):
    author = UserModelUsernameSerializer()

    class Meta:
        model = Topic
        fields = (
            "name",
            "title",
            "description",
            "author",
            "url_name",
        )


class TopicRetrieveSerializer(serializers.ModelSerializer):
    author = UserModelUsernameSerializer()
    posts = SerializerMethodField()

    class Meta:
        model = Topic
        fields = (
            "id",
            "name",
            "title",
            "description",
            "author",
            "url_name",
            "author",
            "posts",
            "created_at",
            "updated_at",
        )

    def get_posts(self, instance):
        return NestedPostSerializer(
            Post.objects.filter(topic=instance).order_by("-updated_at")[:5], many=True
        ).data


class TopicCreateUpdateDeleteSerializer(serializers.ModelSerializer):
    author = UserModelUsernameSerializer(read_only=True)

    class Meta:
        model = Topic
        fields = (
            "name",
            "title",
            "description",
            "author",
        )
