from django.shortcuts import render
from django.views.decorators.cache import cache_page

# Create your views here.
@cache_page(30)
def file_cache(request):
    return render(request,'file_cache.html')
