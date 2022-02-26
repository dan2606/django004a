from django.shortcuts import render

# Create your views here.
def home(request):
    info = "daniel"
    return render(request, "index.html", {"info": info})