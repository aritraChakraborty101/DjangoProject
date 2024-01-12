from django.shortcuts import render
from . import models

# Create your views here.
def list_patients(request):
    all_patients = models.Patient.objects.all()
    context = {'all_patients': all_patients}
    return render(request, 'office/list.html', context = context)