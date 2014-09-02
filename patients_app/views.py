from django.shortcuts import render, get_object_or_404

from .models import Patient


def index(request):
    patients_list = Patient.objects.order_by('-name')
    context = {'patients_list': patients_list}
    return render(request, 'patients_app/index.html', context)


def edit(request, last_name):
    patient = get_object_or_404(Patient, name=last_name)
    return render(request, 'patients_app/edit.html', {'patient': patient})
