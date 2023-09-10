from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
from app.forms import *
# Create your views here.
def insert_std(request):
    sfeo=StudentForms()
    d={'sfeo':sfeo}
    if request.method=='POST':
        sdf=StudentForms(request.POST)
        if sdf.is_valid():
            sid=sdf.cleaned_data['sid']
            sname=sdf.cleaned_data['sname']
            sage=sdf.cleaned_data['sage']
            so=Student.objects.get_or_create(sid=sid,sname=sname,sage=sage)[0]
            so.save()
            qso=Student.objects.all()
            d1={'qso':qso}
            return render(request,'disp_std.html',d1)
        else:
            return HttpResponse('invalid')

    return render(request,'insert_std.html',d)