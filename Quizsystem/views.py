from .forms import studForm,teachForm
from django.shortcuts import render
from django.contrib.auth.models import User
from django.template import RequestContext

def studregi(request):
    context = RequestContext(request)

    registered = False

    if request.method == 'POST':
        stud_form = studForm(data=request.POST)

        if stud_form.is_valid():
            user = stud_form.save()

            user.set_password(user.password)
            user.save()
            registered = True

        else:
            print(stud_form.errors)

    else:
        stud_form = studForm()

    return render(request, 'studregi.html', {'stud_form': stud_form,  'registered': registered})

def teachregi(request):
    context = RequestContext(request)

    registered = False

    if request.method == 'POST':
        teach_form = teachForm(data=request.POST)

        if teach_form.is_valid():
            user = teach_form.save()

            user.set_password(user.password)
            user.save()
            registered = True

        else:
            print(teach_form.errors)

    else:
        teach_form = teachForm()

    return render(request, 'teachregi.html', {'teach_form': teach_form,  'registered': registered})

def select(request):
    return render(request ,'select.html')


