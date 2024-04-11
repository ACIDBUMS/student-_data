from django.shortcuts import render,redirect
from django.http import HttpResponse
from.models import chai,Form


# Create your views here.
def mala (request):
    chaivala=chai.objects.all()
    return render(request,'tempcss.html',{'chaivala': chaivala})

def home(request):
    formats2=Form.objects.all()
    return render(request,'form.html',{'formats2': formats2})

def add (request):
    if request.method == "POST":
        name=request.POST.get('name')
        description=request.POST.get('description')
        email=request.POST.get('email')
        image=request.FILES.get('image')
        form=Form(name=name,description=description,email=email,image=image)
        form.save()
        return redirect('/')


    
    return render(request,'mlist.html',)
