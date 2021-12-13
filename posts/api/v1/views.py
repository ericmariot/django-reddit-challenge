"""
API V1: Posts Views
"""
###
# Libraries
###
from rest_framework import viewsets
from helpers.permissions import IsAuthorOrReadOnly

from topics.models import Topic
from posts.models import Post
from posts.api.v1.serializers import (
    PostSerializer,
    PostRetrieveSerializer,
    PostCreateUpdateDeleteSerializer,
)

###
# Filters
###


###
# Viewsets
###
class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthorOrReadOnly]

    def get_queryset(self):
        topic = Topic.objects.get(url_name=self.kwargs["topic_url_name"])
        return Post.objects.filter(topic=topic.id)

    def perform_create(self, serializer):
        topic = Topic.objects.get(url_name=self.kwargs["topic_url_name"])
        serializer.save(author=self.request.user, topic=topic)

    def get_serializer_class(self):
        if self.action == "list":
            return PostSerializer
        if self.action == "retrieve":
            return PostRetrieveSerializer

        return PostCreateUpdateDeleteSerializer
