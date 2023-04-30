from notes.views.imports import *


class NotesListAndCreate(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        context = {}
        notes = Note.objects.filter(owner=request.user)
        if notes:
            context['notes'] = NoteSerializer(notes, many=True).data
            status_code = HTTP_200_OK
        else:
            context['msg'] = "You haven't added a note!"
            status_code = HTTP_404_NOT_FOUND
        return Response(context, status=status_code)

    @swagger_auto_schema(request_body=NoteDTO)
    def post(self, request):
        context = {}
        note = Note(
            body=request.data.get('body'),
            owner=request.user
        )
        note.save()
        context['note'] = NoteSerializer(instance=note, many=False).data
        return Response(context, status=HTTP_200_OK)
