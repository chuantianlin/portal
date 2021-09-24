from django.contrib import messages
from django.shortcuts import redirect, render
from . forms import *
from django.views import generic
from youtubesearchpython import VideosSearch 

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
def youtube(request):
    if request.method=="POST":
        form=Dashform(request.POST)
        text=request.POST['text']
        video=VideosSearch (text,limit=10)
        result_list=[]
        for i in video.result()['result']:
            result_dict={
                'input':text,
                'title':i['title'],
                'duration':i['duration'],
                'thumbanils':i['thumbnails'][0]['url'],
                'channel':i['channel']['name'],
                'link':i['link'],
                'views':i['viewCount']['short'],
                'publishedtime':i['publishedTime']
            }
            desc=''
            if i['descriptionSnippet']:
                for j in i['descriptionSnippet']:
                    desc+=j['text']
            result_dict['description']=desc
            result_list.append(result_dict)
            context={
                'form':form,   
                'results':result_list
            }
        

        return render(request,"dashboard/youtube.html",context)

    else:
        form=Dashform()
    context={'form':form}
    return render(request,"dashboard/youtube.html",context)
def todo(request):
    form=Todoform(request.POST)
    todo=Todo.objects.filter(user=request.user)
    context={
        'form':form,
        'todos':todo
    }
    return render(request,"dashboard/todo.html",context)
           

     
      
   

        

