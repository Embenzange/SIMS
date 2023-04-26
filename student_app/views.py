from django.shortcuts import render

# Create your views here.
#FrontEnd
def frontend(request):
    return render(request, "frontend.html")

def backend(request):
    return render(request, "backend.html")