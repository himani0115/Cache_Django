from django.urls import path
from . import views
urlpatterns = [
    path('file_cache/',views.file_cache,name='file_cache'),

]
