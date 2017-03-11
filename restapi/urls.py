# Django REST framework
from django.conf.urls import url, include

from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from restapi import views as restapi

router = routers.DefaultRouter()
router.register(r'users', restapi.UserViewSet)
router.register(r'group', restapi.GroupViewSet)

## Wire up our API using automatic URL routing.
## Additionally, we include login URLs for the browsable API.

tutorial = [
url(r'^snippets/$', restapi.SnippetList.as_view()),
    url(r'^snippets/(?P<pk>[0-9]+)/$', restapi.SnippetDetail.as_view()),
]

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include(tutorial))
]

urlpatterns = format_suffix_patterns(tutorial)