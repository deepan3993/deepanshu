
from django.conf.urls import url
from django.contrib import admin
from . import view as base_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', base_view.index),
]
