from django.urls import path,include
from django.conf.urls import url
from . import views
urlpatterns = [ 
path('', views.index),
path('h/',views.index1),
path('s/',views.index2),
path('a/',views.index3),
path('c/',views.index4),
path('l/',views.index5),
path('d/',views.index6),
path('o/',views.index7),
path('k/',views.index8),
 ]