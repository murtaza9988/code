from django.shortcuts import redirect, render
from .models import student
from .forms import *
def student_table(request):
    data=student.objects.all()
    context={
        'student':data
    }
    return render(request,'index.html',context)
def student_data(request):
    if request.method == 'POST':
        form = students_data(request.POST)
        if form.is_valid():
            form.save()
        else:
            return ('error')  # Redirect to a view that lists the students
    else:
        form = students_data
    return render(request, 'input.html', {'form': form})    