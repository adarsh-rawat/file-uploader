from django.conf.urls import url, include 
from rest_framework.routers import DefaultRouter
from apps.notes.views import NoteViewSet
from django.urls import path
from .views import FileUploadAPIView

router = DefaultRouter()
router.register("notes", NoteViewSet, basename="notes")
notes_urlpatterns = [url("api/v1/", include(router.urls)),
                     path('upload-file/', FileUploadAPIView.as_view(), name='upload-file'),]