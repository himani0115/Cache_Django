from django.shortcuts import render
from django.views.decorators.cache import cache_page

# Create your views here.
@cache_page(30)
def mem_cache(request):
    return render(request,'mem_cache.html')
