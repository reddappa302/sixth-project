from django.shortcuts import render

# Create your views here.
def violet(request):
    return render(request,'violet.html')

def indigo(request):
    return render(request,'indigo.html')

def blue(request):
    return render(request,'blue.html')        
