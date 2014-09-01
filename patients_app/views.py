from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from patients_app.models import Patient
from django.http import Http404


def index(request):
    patients_list = Patient.objects.order_by('-name')
    context = {'patients_list': patients_list}
    return render(request, 'patients_app/index.html',context)    

def edit(request, name):
    try:
        patient = Patient.objects.get(name=name)
    except:
        Patient.DoesNotExist:
            raise Http404
    return render(request, 'patients_app/edit.html', {'patient':patient})    
    
    



