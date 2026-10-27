from django.shortcuts import render, redirect
from DB_Learning.models import Student
from django.http import HttpResponse
# Create your views here.
def show_data(request):
    std_data = Student.objects.all()
    print(std_data)
    return render(request, 'data.html', {"data": std_data})

def store_data(request):
    if request.method == "POST":
        name = request.POST.get('name')
        age = request.POST.get('age')
        department = request.POST.get('department')

        if name and age and department:
            Student.objects.create(name = name, age = age, department = department)
            return HttpResponse(f"Hii {name} ! You have successfully submit your response")
        else:
            return HttpResponse("Please fill All the sections")
    # return redirect('data.html')
        

