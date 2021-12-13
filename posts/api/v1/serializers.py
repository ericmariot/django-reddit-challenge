"""
API V1: Posts Serializers
"""

###
# Libraries
###
from rest_framework import serializers

from accounts.api.v1.serializers import UserModelUsernameSerializer
from posts.models import Post
###
# Serializers
class PostSerializer(serializers.ModelSerializer):
    author = UserModelUsernameSerializer()
    topic = "topics.TopicSerializer"

    class Meta:
        model = Post
        fields = (
            "id",
            "title",
            "content",
            "upvotes",
            "author",
            "topic",
        )


class PostRetrieveSerializer(serializers.ModelSerializer):
    author = UserModelUsernameSerializer()
    topic = "topics.TopicSerializer"

    class Meta:
        model = Post
        fields = (
            "id",
            "title",
            "content",
            "upvotes",
            "author",
            "topic",
            "created_at",
            "updated_at",
        )


class PostCreateUpdateDeleteSerializer(serializers.ModelSerializer):
    author = UserModelUsernameSerializer(read_only=True)
    topic = serializers.ReadOnlyField(source="topic.url_name")

    class Meta:
        model = Post
        fields = (
            "title",
            "content",
            "author",
            "topic",
            "created_at",
            "updated_at",
        )


class NestedPostSerializer(serializers.ModelSerializer):
    author = UserModelUsernameSerializer(read_only=True)

    class Meta:
        model = Post
        fields = (
            "title",
            "content",
            "author",
        )
