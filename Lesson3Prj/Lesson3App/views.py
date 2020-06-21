from django.shortcuts import render
from Lesson3App.models import Student
from django.core.paginator import Paginator

# Create your views here.
def list(request):
    #std=Student.objects.all()
   # std=Student.objects.order_by('email')
    std=Student.objects.all()
    paginator=Paginator(std,10)
    page=request.GET.get('page')
    students=paginator.get_page(page)
    context={'students':students,'title':'List'}
    return render(request,'list.html',context)