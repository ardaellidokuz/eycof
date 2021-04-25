from django.urls import path

from . import views
app_name='basemap'
urlpatterns = [
    path('', views.index, name='index'),
    path('login',views.loggingin, name='login'),
    path('register',views.register,name='register'),
    path('logout',views.loggingout,name='logout'),
    path('account',views.accountinfo,name='account'),
    path('passwordchange',views.passwordchange,name='passwordchange'),
]