from django.urls import path

from . import views
##For mapping
urlpatterns = [
    path('',views.home,name='Home'),
    path('add',views.add,name='Addition')
]
