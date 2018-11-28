from django.conf.urls import url
from .views import index, signup

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^signup/$', signup, name='signup'),
]
