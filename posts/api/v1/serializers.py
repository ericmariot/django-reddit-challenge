"""
API V1: Posts Serializers
"""

###
# Libraries
###
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from accounts.api.v1.serializers import UserModelUsernameSerializer
from comments.models import Comment
from comments.api.v1.serializers import (
    NestedCommentSerializer,
)
from posts.models import Post

###
# Serializers
class PostSerializer(serializers.ModelSerializer):
    author = UserModelUsernameSerializer()
    topic = serializers.ReadOnlyField(source="topic.url_name")
    upvotes = serializers.IntegerField(source="total_upvotes")

    class Meta:
        model = Post
        fields = (
            "id",
            "title",
            "content",
            "upvotes",
            "topic",
            "author",
        )


class PostRetrieveSerializer(serializers.ModelSerializer):
    author = UserModelUsernameSerializer()
    topic = serializers.ReadOnlyField(source="topic.url_name")
    comments = SerializerMethodField()
    upvotes = serializers.IntegerField(source="total_upvotes")

    class Meta:
        model = Post
        fields = (
            "id",
            "title",
            "content",
            "upvotes",
            "topic",
            "author",
            "comments",
            "created_at",
            "updated_at",
        )

    def get_comments(self, instance):
        return NestedCommentSerializer(
            Comment.objects.filter(post=instance).order_by("-updated_at")[:5], many=True
        ).data


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
