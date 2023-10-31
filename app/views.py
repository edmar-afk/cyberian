from django.shortcuts import redirect, render
from .models import Students
from django.contrib import messages
from django.db.models import Sum
# Create your views here.


def home(request):

    total_amount = Students.objects.all()
    students_count = Students.objects.all().count()
    students_lists = Students.objects.all().order_by('-id')
    
    # Calculate the total amount using the aggregate function
    total_amount = Students.objects.aggregate(total_amount=Sum('amount'))['total_amount']


    if request.method == 'POST':
        name = request.POST['name']
        year = request.POST['year']
        amount = request.POST['amount']

        new_fees = Students(name=name, year=year, amount=amount)
        new_fees.save()
        messages.success(request, 'Student Added!')
        return redirect('/home')
    context = {
        'students_count': students_count,
        'students_lists': students_lists,
        'total_amount': total_amount,

    }
    return render(request, 'index.html', context)


def deleterecord(request, stud_id):
    Students.objects.filter(id=stud_id).delete()
    messages.error(request, 'Student Deleted!')
    return redirect('/home') 
