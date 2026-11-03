from django.shortcuts import render, redirect
from to_do_list_app.models import To_Do_List
# Create your views here.
def home(request):
    data = To_Do_List.objects.all()
    return render(request, 'home.html', {'data':data})



def add_task(request):
    if request.method =="POST":
        title = request.POST.get('title')
        description = request.POST.get('description')

        if title and description:
            To_Do_List.objects.create(title = title, description = description)
            return redirect('home')
    return render(request, 'add_task.html')


def edit_task(request, id):
    std_id = To_Do_List.objects.get(id=id)
    print("Std_id_data", std_id)
    if request.method =="POST":
        title = request.POST.get('title')
        description = request.POST.get('description')

        if title and description:
            std_id.title = title
            std_id.description=description
            std_id.save()
            return redirect('home')

        def __str__(self):
            return self.title
    return render(request, 'edit_task.html', {'std_id':std_id})

def delete_task(request, id):
    std_id = To_Do_List.objects.get(id = id)
    std_id.delete()
    return redirect('home')

def update_task(request,id):
    task_update=To_Do_List.objects.get(id=id)
    # if request.method=="POST":
    task=request.POST.get('done')=="True"
    task_update.done=task
    task_update.save()
    return redirect('home')







