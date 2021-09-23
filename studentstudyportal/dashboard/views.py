from django.contrib import messages
from django.shortcuts import redirect, render
from . forms import *
from django.views import generic


def home(request):
    return render(request,'dashboard/home.html')

def notes(request):
    if request.method=="POST":
        form=NoteForm(request.POST)
        if form.is_valid():
            notes=Notes(user=request.user,title=request.POST['title'],description=request.POST['description'])
            notes.save()
        messages.success(request,f"add notes from{request.user.username} Sucessfully")
    else:
        form=NoteForm()
    notes=Notes.objects.filter(user=request.user)#login user data
    context={'notes':notes,'form':form}
    return render(request,'dashboard/notes.html',context)

def delete_note(request,pk=None):
    Notes.objects.get(id=pk).delete()
    return redirect("notes")
class NoteDetailView(generic.DetailView):
    model=Notes

def HomeWork(request):
        if request.method =="POST":
            form=HomeworkForm(request.POST)
            if form.is_valid():
                try:
                    finished=request.POST['is_finished']
                    if finished=='on':
                        finished=True
                    else:
                        finished=False
                except:
                        finished=False
                homeworks=Homework(user= request.user,subject=request.POST['subject'],
            title=request.POST['title'],
            description=request.POST['subject'],
            due=request.POST['due'],
            is_finished=finished)
            
            homeworks.save()

        form=HomeworkForm()
        homework=Homework.objects.filter(user=request.user)
        
        if len(homework)==0:
                Homework_done=True
        else:
                Homework_done=False
        context={'homeworks':homework,'homeworks_done':Homework_done,'form':form}
        return render(request,'dashboard/homework.html',context)

   
def Homewor_Delete(request,pk=None):
     Homework.objects.get(id=pk).delete()
     return redirect("homework")

# Create your views here.
