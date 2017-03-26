# Django REST framework
from django.conf.urls import url, include

from rest_framework.urlpatterns import format_suffix_patterns

from restapi import views as restapi

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

# API endpoints
urlpatterns = format_suffix_patterns([
    url(r'^$', restapi.api_root),
    url(r'^snippets/$',
        restapi.SnippetList.as_view(),
        name='snippet-list'),
    url(r'^snippets/(?P<pk>[0-9]+)/$',
        restapi.SnippetDetail.as_view(),
        name='snippet-detail'),
    url(r'^snippets/(?P<pk>[0-9]+)/highlight/$',
        restapi.SnippetHighlight.as_view(),
        name='snippet-highlight'),
    url(r'^users/$',
        restapi.UserList.as_view(),
        name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$',
        restapi.UserDetail.as_view(),
        name='user-detail'),
])

# Login and logout views for the browsable API.

urlpatterns += [
    url(r'^api-auth/', include('rest_framework',
                               namespace='rest_framework')),
]