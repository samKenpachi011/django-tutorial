#import URLConf,path,views
from django.urls import path

from . import views

#django will automatically look for this object
urlpatterns = [
path('',views.index, name='index'),
]

