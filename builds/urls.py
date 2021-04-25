from django.urls import path

from . import views
app_name='builds'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:build_id>/', views.detail, name='detail'),
    path('<int:build_id>/results/', views.results, name='results'),
    path('add/', views.add, name='add'),
    path('<int:build_id>/voteplus/',views.voteplus,name='voteplus'),
    path('<int:build_id>/voteminus/',views.voteminus,name='voteminus'),
    path('mybuildorders/',views.mybuildorders, name='mybuildorders'),
    path('<int:build_id>/changebuild/',views.changebuild,name='changebuild'),
    path('search/',views.search,name='search'),
    path('<int:build_id>/deletebuild/',views.deletebuild,name='deletebuild')
]