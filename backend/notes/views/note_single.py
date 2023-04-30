from .imports import *
from ..dto import NoteEditDTO


class NoteSingle(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(responses={200: NoteDTO})
    def get(self, request, pk):
        context = {}
        try:
            note = Note.objects.get(pk=pk, deleted=False, owner=request.user)
            context['note'] = NoteSerializer(instance=note, many=False).data
            status_code = HTTP_200_OK
        except:
            context['msg'] = "Note not found!"
            status_code = HTTP_404_NOT_FOUND
        return Response(context, status=status_code)

    @swagger_auto_schema()
    def delete(self, request, pk):
        context = {}
        try:
            note = Note.objects.get(pk=pk, deleted=False, owner=request.user)
            context['msg'] = f"Note with id {note.id} deleted"
            note.delete()
            status_code = HTTP_200_OK
        except:
            context['msg'] = "Note not found!"
            status_code = HTTP_404_NOT_FOUND
        return Response(context, status=status_code)

    @swagger_auto_schema(responses={200: NoteDTO}, request_body=NoteEditDTO)
    def put(self, request, pk):
        context = {}
        try:
            note = Note.objects.get(pk=pk, deleted=False, owner=request.user)
            note.body = request.data.get('body')
            note.save()
            status_code = HTTP_200_OK
        except:
            context['msg'] = "Note not found!"
            status_code = HTTP_404_NOT_FOUND
        return Response(context, status=status_code)


class NoteCreate(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(responses={200: NoteDTO}, request_body=NoteEditDTO)
    def post(self, request):
        context = {}
        try:
            note = Note(body=request.data.get('body'), owner=request.user)
            note.save()
            context['note'] = NoteSerializer(instance=note, many=False).data
            status_code = HTTP_200_OK
        except:
            context['msg'] = "Invalid request!"
            status_code = HTTP_400_BAD_REQUEST
        return Response(context, status=status_code)
