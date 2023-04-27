from django.shortcuts import render
from django.contrib.auth.decorators import login_required #Login required to access private pages
from django.views.decorators.cache import cache_control #Prevent back button once you logout until you login again 
# Create your views here.
#FrontEnd
def frontend(request):
    return render(request, "frontend.html")

@login_required(login_url="login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def backend(request):
    return render(request, "backend.html")