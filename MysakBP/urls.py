from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^work$', views.work, name='work'),
    url(r'^upload$', views.uploadImage, name='upload_image'),
    url(r'$', views.layout, name='layout'),
]