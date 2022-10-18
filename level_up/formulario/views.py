from django.shortcuts import redirect, render

from .forms import StudentForm
from .models import Formul, Formul2

# Create your views here.



def create_form(request):
    form = StudentForm()

    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('form-create')

    context = {
        'form': form,
    }
    return render(request, 'formulario/create.html', context)

def form_list(request):
    employees = Formul2.objects.all()
    context = {
        'employees': employees,
    }
    return render(request, 'formulario/list.html', context)