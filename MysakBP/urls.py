from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^work$', views.work, name='work'),
    url(r'^upload$', views.uploadImage, name='upload_image'),

    url(r'get_files/(?P<user>\w+)$', views.getFiles, name='get_files'),
    url(r'(?P<user>\w+)$', views.layout, name='layout'),
    url(r'^$', views.login, name='login'),
]