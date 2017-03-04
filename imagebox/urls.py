from django.conf.urls import url

from imagebox import views

app_name = 'imagebox'

urlpatterns = [
    url(r'^$', views.model_form_upload, name='image_upload'),
]