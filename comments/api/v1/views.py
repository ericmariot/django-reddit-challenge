"""
API V1: Comments Views
"""
###
# Libraries
###
from rest_framework import viewsets
from helpers.permissions import IsAuthorOrReadOnly

from posts.models import Post
from comments.models import Comment
from comments.api.v1.serializers import (
    CommentSerializer,
    CommentRetrieveSerializer,
    CommentCreateUpdateDeleteSerializer,
)

###
# Filters
###


###
# Viewsets
###
class CommentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthorOrReadOnly]

    def get_queryset(self):
        post = Post.objects.get(id=self.kwargs["post_pk"])
        return Comment.objects.filter(post=post)

    def perform_create(self, serializer):
        post = Post.objects.get(id=self.kwargs["post_pk"])
        serializer.save(author=self.request.user, post=post)

    def get_serializer_class(self):
        if self.action == "list":
            return CommentSerializer
        if self.action == "retrieve":
            return CommentRetrieveSerializer

        return CommentCreateUpdateDeleteSerializer
