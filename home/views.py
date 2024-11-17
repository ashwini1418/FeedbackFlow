from django.shortcuts import render

# Create your views here.
def index(request):
    context={
        'variable':"this is sent"
    }
    return render(request, "index.html", context)
def login(request):
    return render(request,"pages-login.html",)

def signup(request):
    return render(request, "pages-signup.html", )

