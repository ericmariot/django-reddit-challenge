"""
API V1: Topics Serializers
"""

###
# Libraries
###
from rest_framework import serializers
from topics.models import Topic
from accounts.api.v1.serializers import UserModelUsernameSerializer

###
# Serializers
class TopicSerializer(serializers.ModelSerializer):
    author = UserModelUsernameSerializer()

    class Meta:
        model = Topic
        fields = (
            "title",
            "description",
            "author",
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