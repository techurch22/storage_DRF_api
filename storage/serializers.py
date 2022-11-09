from rest_framework import serializers
from .models import Storage
from .cyph import Cypher



class StorageSerializer(serializers.Serializer):
    code_phrase = serializers.CharField(max_length=100)
    storage_content = serializers.CharField()
    secret_key = serializers.CharField(max_length=20, read_only=True)
    created = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return Storage.objects.create(
            **validated_data,
            secret_key=Cypher.get_key()
        )
