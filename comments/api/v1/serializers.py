"""
API V1: Comments Serializers
"""

###
# Libraries
###
from rest_framework import serializers

from accounts.api.v1.serializers import UserModelUsernameSerializer
from comments.models import Comment

###
# Serializers
class CommentSerializer(serializers.ModelSerializer):
    author = UserModelUsernameSerializer()
    post = serializers.ReadOnlyField(source='post.title')

    class Meta:
        model = Comment
        fields = (
            "id",
            "title",
            "content",
            "upvotes",
            "author",
            "post",
        )


class CommentRetrieveSerializer(serializers.ModelSerializer):
    author = UserModelUsernameSerializer()
    post = serializers.ReadOnlyField(source='post.title')

    class Meta:
        model = Comment
        fields = (
            "id",
            "title",
            "content",
            "upvotes",
            "author",
            "post",
            "created_at",
            "updated_at",
        )


class CommentCreateUpdateDeleteSerializer(serializers.ModelSerializer):
    author = UserModelUsernameSerializer(read_only=True)
    post = serializers.ReadOnlyField(source="post.title")

    class Meta:
        model = Comment
        fields = (
            "title",
            "content",
            "author",
            "post",
            "created_at",
            "updated_at",
        )


class NestedCommentSerializer(serializers.ModelSerializer):
    author = UserModelUsernameSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = (
            "title",
            "content",
            "upvotes",
            "author",
        )
