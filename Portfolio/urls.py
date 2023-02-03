from django.urls import path

from . import views
##For mapping
urlpatterns = [
    path('',views.ProfileHome,name='Profile'),
]
