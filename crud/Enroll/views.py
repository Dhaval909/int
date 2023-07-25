from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import User


# Create your views here.
# This func add new items and show all items
def add_show(request):
    try:
        if request.method == 'POST':                 #creating object for rendering form
            fm = StudentRegistration(request.POST)
            # if fm.is_valid():            # short trick to save data to admin. only working on ModelForm not on forms.Form.
            #     fm.save()
            if fm.is_valid():
                nm = fm.cleaned_data['name']
                em = fm.cleaned_data['email']
                pw = fm.cleaned_data['password']           #dont mention password if if you dont save password.
                reg = User(name=nm,email=em,password=pw)
                reg.save()
                fm = StudentRegistration()                 # after click submit blank user data to form.
        else:
            fm = StudentRegistration()
            
        stud = User.objects.all()
    except:
        pass
    return render(request,'Temp_enroll/addnshow.html', {'form':fm, 'stu':stud})

# delete func
def delete_data(request,id):
    if request.method=='POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')

# update func
def update_data(request,id):
    if request.method=='POST':
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)
            
    return render(request,'Temp_enroll/update.html',{'form':fm})