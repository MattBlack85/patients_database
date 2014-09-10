from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import Patient
from visits_app.models import Visit
from visits_app.forms import VisitForm
from django.http import Http404


def index(request):
    patients_list = Patient.objects.order_by('-last_name')
    context = {'patients_list' : patients_list}
    return render(request, 'patients_app/index.html',context)    

def edit(request,pk):
    print request.POST
    patient = get_object_or_404(Patient,pk=pk)
    #visits = Visit.objects.filter(patient=Patient.objects.get(pk=pk))
    #v_action = "/patients_app/" + str(patient.pk) +"/edit/"
    visits = Visit.objects.select_related('patient').filter(patient=patient)
          
    v_form = VisitForm(request.POST or None)
    if v_form.is_valid():
        description = v_form.save(commit=False)
        description.post = post
        description.save
        
     
    return render(request, 'patients_app/edit.html', {'patient':patient, 'visits': visits, 'v_form': v_form})    


    

