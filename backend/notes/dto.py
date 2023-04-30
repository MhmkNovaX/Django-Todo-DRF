from rest_framework import serializers


class NoteDTO(serializers.Serializer):
    id = serializers.IntegerField()
    body = serializers.CharField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()


class NoteEditDTO(serializers.Serializer):
    body = serializers.CharField()
