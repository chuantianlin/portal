from django.conf import urls
from django.urls import path
from django.urls.resolvers import URLPattern
from . import views
urlpatterns=[
    path('',views.home),
    path('notes/',views.notes,name="notes"),
    path('delete_notes/<int:pk>',views.delete_note,name="delete_note"),
    path('notes_detail/<int:pk>',views.NoteDetailView.as_view(),name="notes_detail"),
    path('homework/',views.HomeWork,name="homework"),
    path('homework_delete/<int:pk>',views.Homewor_Delete,name="homework_delete"),
]