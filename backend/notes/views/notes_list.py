from .imports import *


class NotesList(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(responses={200: NoteDTO})
    def get(self, request):
        context = {}
        q = Q(deleted=False, owner=request.user)
        if request.GET.get('search'):
            q = q & Q(body__icontains=request.GET.get('search'))
        notes = Note.objects.filter(q)
        status_code = HTTP_404_NOT_FOUND
        if notes:
            context['notes'] = NoteSerializer(instance=notes, many=True).data
            status_code = HTTP_200_OK
        else:
            context['msg'] = "You haven't added a note!"
        return Response(context, status=status_code)
