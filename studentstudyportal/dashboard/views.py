from django.contrib import messages
from django.shortcuts import redirect, render
from . forms import *
from django.views import generic
from youtubesearchpython import VideosSearch 
import requests
import wikipedia
 

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
    if request.method=='POST':
        form=Todoform(request.POST)
        if form.is_valid():
            try:
                finished=request.POST["is_finished"]
                if finished=='on':
                    finished= True
                else:
                    finished=False
            except:

                    finished=False
            todo=Todo(user=request.user,title=request.POST['title'],is_finished=finished)
            todo.save()
    else:
        form=Todoform()
    todos=Todo.objects.filter(user=request.user)
    if len(todos)==0:
        todos_done=True
    else :
        todos_done=False
    context={
        'form':form,
        'todos':todos,
        'todos_done':todos_done

    }
    return render(request,"dashboard/todo.html",context)
def todo_delete(request,pk=None):  

     Todo.objects.get(id=pk).delete()
     return redirect("todo")
def todo_update(request,pk=None):  

    todo=Todo.objects.get(id=pk)
    if todo.is_finished==True:
        todo.is_finished=False
    else:
        todo.is_finished=True
    
    return redirect("todo")

           
def book(request):
    if request.method=="POST":
        form=Dashform(request.POST)
        text=request.POST['text']

        url="https://www.googleapis.com/books/v1/volumes?q="+text
        r=requests.get(url)
        answer=r.json()
        result_list=[]
        for i in range(10):
            result_dict={
               
                'title':answer['items'][i]['volumeInfo']['title'],
                'subtitle':answer['items'][i]['volumeInfo'].get('subtitle'),
                'description':answer['items'][i]['volumeInfo'].get('description'),
                'count':answer['items'][i]['volumeInfo'].get('PageCount'),
                'catagories':answer['items'][i]['volumeInfo'].get('catagories'),
                'rating':answer['items'][i]['volumeInfo'].get('pageRating'),
                'thumbnail':answer['items'][i]['volumeInfo'].get('imageLinks').get('thumbnail'),
                'preview':answer['items'][i]['volumeInfo'].get('previewLink'),
            }
           
            result_list.append(result_dict)
            context={
                'form':form,   
                'results':result_list
            }
        

        return render(request,"dashboard/books.html",context)

    else:
        form=Dashform()
    context={'form':form}
    return render(request,"dashboard/books.html",context)

def dictionary(request):
    if request.method=="POST":
        form=Dashform(request.POST)
        h=request.POST['text']
        url="https://api.dictionaryapi.dev/api/v2/entries/en_US/"+h
        r=requests.get(url)
        answer=r.json()
        try:
            phonetics=answer[0]['phonetics'][0]['text']
            audio=answer[0]['phonetics'][0]['audio']
            definition=answer[0]['meanings'][0]['definitions'][0]['definition']
            example=answer[0]['meanings'][0]['definitions'][0]['example']
            synonyms=answer[0]['meanings'][0]['definitions'][0]['synonyms']
            context={
                'form':form,
                'input':h,
                'phonetics':phonetics,
                'audio':audio,
                'definition':definition,
                'example':example,
                'synonyms':synonyms
            }
        except:
            context={
                'form':form,
                'input':''
            }    
        return render(request,"dashboard/dictionary.html",context)

    else:
        form=Dashform()
    context={'form':form}
    return render(request,"dashboard/dictionary.html",context)
def wiki(request):
    if request.method=="POST":
        form=Dashform(request.POST)
        text=request.POST['text']
        search=wikipedia.page(text)
      
   
        context={
                'form':form,
                'title':search.title,
                'link':search.url,
                'details':search.summary
            }    
        return render(request,"dashboard/wiki.html",context)

    else:
        form=Dashform()
        context={'form':form}
    return render(request,"dashboard/wiki.html",context)
def conversion(request):
    form=conversion
    context={'form':form ,'input':False}
    return render(request,"dashboard/conversion.html",context)
    
   
   
      
   

        

