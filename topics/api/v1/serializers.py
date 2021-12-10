"""
API V1: Topics Serializers
"""

###
# Libraries
###
from rest_framework import serializers
from rest_auth.serializers import (
    UserDetailsSerializer as BaseUserDetailsSerializer,
)

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
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["author"] = BaseUserDetailsSerializer(instance.author).data

        return data

    class Meta:
        model = Topic
        fields = (
            "name",
            "title",
            "description",
            "author",
        )