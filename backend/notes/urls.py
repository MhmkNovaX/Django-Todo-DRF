from django.urls import path, include


urlpatterns = [
    path('api/', include('notes.views.api.urls'))
]