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
    return render(request, 'patients_app/index.html', context)

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
