from django.contrib.auth.hashers import make_password
from rest_framework.permissions import *
from rest_framework.response import Response
from rest_framework.status import *
from rest_framework.views import APIView

from user.models import User
from user.serializers import UserSerializer