from notes.views.imports import *


class NoteSingle(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        context = {}
        try:
            note = Note.objects.get(pk=pk, owner=request.user)
            context['note'] = NoteSerializer(note).data
            status_code = HTTP_200_OK
        except:
            context['msg'] = "Note not found!"
            status_code = HTTP_404_NOT_FOUND
        return Response(context, status=status_code)

    def delete(self, request, pk):
        context = {}
        try:
            note = Note.objects.get(pk=pk, owner=request.user)
            context['msg'] = f"Note with id {note.id} deleted"
            note.delete()
            status_code = HTTP_200_OK
        except:
            context['msg'] = "Note not found!"
            status_code = HTTP_404_NOT_FOUND
        return Response(context, status=status_code)

    @swagger_auto_schema(request_body=NoteDTO)
    def put(self, request, pk):
        context = {}
        try:
            note = Note.objects.get(pk=pk, owner=request.user)
            note.body = request.data.get('body')
            note.save()
            status_code = HTTP_200_OK
        except:
            context['msg'] = "Note not found!"
            status_code = HTTP_404_NOT_FOUND
        return Response(context, status=status_code)
