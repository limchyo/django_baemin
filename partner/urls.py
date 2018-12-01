from django.conf.urls import url
from .views import (
    index, signup, login, logout, edit_info
)

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^signup/$', signup, name='signup'),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^edit_info/$', edit_info, name='edit_info'),
]
