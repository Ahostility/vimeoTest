from django.conf.urls import url
from . import views

urlpatterns = [
    url('video/',views.videoCreate,name='videocreate'),
]