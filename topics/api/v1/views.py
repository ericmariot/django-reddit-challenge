"""
API V1: Topics Views
"""
###
# Libraries
###
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from topics.models import Topic
from topics.api.v1.serializers import (
    TopicRetrieveSerializer,
    TopicSerializer,
)

###
# Filters
###


###
# Viewsets
###
class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.action == "list":
            return TopicSerializer
        if self.action == "retrieve":
            return TopicRetrieveSerializer

        return TopicSerializer