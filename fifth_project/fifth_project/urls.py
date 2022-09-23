from django.contrib import admin
from django.urls import re_path, include
from basic_app import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^special/', views.special, name='special'),
    re_path(r'^basic_app/', include('basic_app.urls')),
    re_path(r'^logout/$', views.user_logout, name='logout')
]


""" urlpatterns = [
    path('', views.index, name='index'),
    path('admin', admin.site.urls),
    path('basic_app/', include('basic_app.urls'))
] """
