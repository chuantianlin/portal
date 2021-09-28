from django.conf import urls
from django.urls import path
from django.urls.resolvers import URLPattern
from . import views
urlpatterns=[
    path('',views.home,name="home"),
    path('notes/',views.notes,name="notes"),
    path('delete_notes/<int:pk>',views.delete_note,name="delete_note"),
    path('notes_detail/<int:pk>',views.NoteDetailView.as_view(),name="notes_detail"),
    path('homework/',views.HomeWork,name="homework"),
    path('youtube/',views.youtube,name="youtube"),
    path('homework_delete/<int:pk>',views.Homewor_Delete,name="homework_delete"),
    path('todo/',views.todo,name="todo"),
    path('todo_delete/<int:pk>',views.todo_delete,name="todo_delete"),
    path('update_todo/<int:pk>',views.todo_update,name="update_todo"),
    path('books/',views.book,name="books"),
    path('dictionary/',views.dictionary,name="dictionary"),
    path('wiki/',views.wiki,name="wiki"),
    path('conversion/',views.conversion,name="conversion"),
   
]