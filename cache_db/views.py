from django.shortcuts import render
from django.views.decorators.cache import cache_page

# Create your views here.
@cache_page(30)
def index(request):

    # user = User.objects.get(username=)
    return render(request,'index.html')
