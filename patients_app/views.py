from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import Patient
from .forms import PatientForm
from visits_app.models import Visit
from visits_app.forms import VisitForm
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def index(request):
    patients_list = Patient.objects.order_by('-last_name')
    if request.method == 'POST':
        if request.POST.get('patient'):
            patient_id = request.POST['patient']
            new_first = request.POST['first_name']
            new_second = request.POST['second_name']
            new_last = request.POST['last_name']
            new_pesel = request.POST['pesel']
            old_patient = patients_list.get(pk=patient_id)
            old_patient.first_name = new_first
            old_patient.second_name = new_second
            old_patient.last_name = new_last
            old_patient.pesel = new_pesel
            old_patient.save()
        else: #there are no patients
            p_form = PatientForm(request.POST)
            if p_form.is_valid():
                p_form.save()
            return render(request, 'patients_app/index.html', {'patients_list':patients_list, 'p_form':p_form})             
    return render(request, 'patients_app/index.html', {'patients_list':patients_list, 'p_form':PatientForm()})

def edit(request, pk):
    patient = get_object_or_404(Patient, pk=pk)  
    visits = Visit.objects.select_related('patient').filter(patient=patient)
    if request.method == 'POST':
        if request.POST.get('visit'):  # The visit exists
            visit_id = request.POST['visit']
            new_description = request.POST['description']
            old_visit = patient.visit_set.get(pk=visit_id)
            old_visit.description = new_description
            old_visit.save()
        else:  # We got a new visit
            v_form = VisitForm(request.POST)
            if v_form.is_valid():
                v_form.save()
            return render(request, 'patients_app/edit.html', {'patient':patient, 'visits': visits, 'v_form': v_form})
    return render(request, 'patients_app/edit.html', {'patient':patient, 'visits': visits, 'v_form': VisitForm()})
