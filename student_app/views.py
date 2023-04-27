from django.shortcuts import render
from django.contrib.auth.decorators import login_required #Login required to access private pages

# Create your views here.
#FrontEnd
def frontend(request):
    return render(request, "frontend.html")
@login_required(login_url="login")
def backend(request):
    return render(request, "backend.html")