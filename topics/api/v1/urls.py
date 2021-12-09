"""
API V1: Topics Urls
"""
###
# Libraries
###
from django.conf.urls import url, include
from rest_framework_nested import routers
from topics.api.v1.views import (
    TopicViewSet,
)

###
# Routers
###
router = routers.SimpleRouter()
router.register(r"topics", TopicViewSet, basename="topics")

###
# URLs
###
urlpatterns = [
    url(r"^", include(router.urls)),
]