from rest_framework import viewsets 
from apps.notes.models import Note 
from apps.notes.serializers import NoteSerializer

class NoteViewSet(viewsets.ModelViewSet):

    serializer_class = NoteSerializer
    queryset = Note.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(created_by=self.request.user)
    

from rest_framework import status
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import NoteSerializer

class FileUploadAPIView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = NoteSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            # you can access the file like this from serializer
            # uploaded_file = serializer.validated_data["file"]
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )