from django.urls import path

from . import views
##For mapping
urlpatterns = [
    path('register',views.register,name='register'),
    path('signin',views.signin,name='signin'),
    path('signout',views.signout,name='signout'),
    path('UserForm',views.UserDetails,name='UserForm'),
]
