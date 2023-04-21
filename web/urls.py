from web import views
from django.urls import path, re_path, include

app_name = 'web'

urlpatterns = [
    path('', views.index, name='index'),
    path('upload', views.upload_data, name='upload_data'),
]
