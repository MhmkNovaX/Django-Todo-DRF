from django.urls import path

from . import NoteSingle, NotesListAndCreate

urlpatterns = [
    path('', NotesListAndCreate.as_view()),
    path('<int:pk>/', NoteSingle.as_view()),
]
