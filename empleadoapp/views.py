from django.shortcuts import render

# Create your views here.

def index_empleadoapp(request):
    return render(request,'index.html')
    
def crear_empleadoapp(request):
    return render(request,'empleadoapp/crear.html')