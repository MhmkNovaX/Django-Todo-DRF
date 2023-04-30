from rest_framework.response import Response
from rest_framework.views import APIView
from notes.models import Note
from notes.selializers import NoteSerializer
from rest_framework.status import *
from rest_framework.permissions import *
from drf_yasg.utils import swagger_auto_schema
from django.contrib.auth.hashers import make_password


from notes.dto import NoteDTO
from user.serializers import UserSerializer
from user.dto import UserDTO
from user.models import User
