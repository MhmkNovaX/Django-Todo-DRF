from rest_framework import serializers


class NoteDTO(serializers.Serializer):
    body = serializers.CharField()
