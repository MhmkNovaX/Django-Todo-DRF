from django.urls import path

from .views import NotesList, NoteSingle, NoteCreate

urlpatterns = [
    path('api/list', NotesList.as_view(), name='NotesList'),
    path('api/single/', NoteCreate.as_view(), name='NotesCreate'),
    path('api/single/<int:pk>/', NoteSingle.as_view(), name='NotesSingleWithPK'),
]