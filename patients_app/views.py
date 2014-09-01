from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from patients_app.models import Patient

def index(request):
    patients_list = Patient.objects.order_by('-name')
    template = loader.get_template('patients_app/index.html')
    context = RequestContext(request, {
        'patients_list': patients_list,
        })
    return HttpResponse(template.render(context))
    

def edit(request, name):
    return HttpResponse("edit patient %s" % name)

