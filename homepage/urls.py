from django.conf.urls import url

from homepage import views as homepage

app_name = 'homepage'

urlpatterns = [
    url(r'^$', homepage.index, name='index'),
    url(r'^about', homepage.about, name='about'),
    url(r'^products', homepage.display_product_images, name='products'),
    url(r'^document', homepage.model_form_upload, name='document'),
]