from rest_framework import views, permissions
from rest_framework.response import Response
from utils.base.renderers import PlainTextRenderer
from django.conf import settings
import os
import logging

log = logging.getLogger(__name__)


class LogViewSet(views.APIView):
    permission_classes = (permissions.IsAdminUser,)

    def get(self, _):
        log_file = open(settings.LOG_FILE_ABS_PATH, 'r')
        text = log_file.read()
        log_file.close()
        return Response(text, status=200)


class LogFileViewSet(views.APIView):
    permission_classes = (permissions.IsAdminUser,)
    renderer_classes = (PlainTextRenderer,)

    def get(self, *args, **kwargs):
        filename = self.kwargs.get("filename")
        dirname = os.path.join(settings.PROJECT_ROOT, "logs")
        dirname = os.path.join(dirname, filename)
        log_file = open(dirname, mode="r", errors="ignore")
        text = log_file.read().encode("utf-8")
        log_file.close()
        return Response(text, status=200)

