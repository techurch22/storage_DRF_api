from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from .models import Storage
from .serializers import StorageSerializer
from rest_framework import views


# Create your views here.

class CreateStorageAPIView(views.APIView):

    def post(self, request):
        storage = StorageSerializer(data=request.data)
        storage.is_valid(raise_exception=True)
        storage.save()

        return Response({"key": storage.data['secret_key']}, status=status.HTTP_200_OK)


class StorageAPIView(views.APIView):

    def post(self, request, key):

        try:
            storage = Storage.objects.get(secret_key=key)
            assert storage.code_phrase == request.data['code_phrase']

        except Storage.DoesNotExist:
            return Response({"error": "key out of base"}, status=status.HTTP_404_NOT_FOUND)

        except AssertionError:
            return Response({"error": "code not pass"}, status=status.HTTP_404_NOT_FOUND)

        serial_storage = StorageSerializer(storage)
        storage.delete()

        return Response({'storage': serial_storage.data['storage_content']})
