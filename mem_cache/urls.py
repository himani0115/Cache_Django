from django.urls import path
from . import views
urlpatterns = [
    path('mem_cache/',views.mem_cache,name='mem_cache'),

]
