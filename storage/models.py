from django.db import models

class Storage(models.Model):
    code_phrase = models.CharField(max_length=100)
    storage_content = models.TextField()
    secret_key = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.created)
