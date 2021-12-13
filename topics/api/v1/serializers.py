"""
API V1: Topics Serializers
"""

###
# Libraries
###
from rest_framework import serializers

from accounts.api.v1.serializers import UserModelUsernameSerializer
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
            "created_at",
            "updated_at",
        )


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
