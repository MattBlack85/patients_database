from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext, loader
from patients_app.models import Patient
from django.http import Http404


def index(request):
    patients_list = Patient.objects.order_by('-last_name')
    context = {'patients_list' : patients_list}
    return render(request, 'patients_app/index.html',context)    

def edit(request,pk):
    patient = get_object_or_404(Patient,pk=pk)
    return render(request, 'patients_app/edit.html', {'patient' : patient})    
    
    



