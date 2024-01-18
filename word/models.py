import uuid

from django.db import models

from account.models import User

class Word(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_by = models.ForeignKey(User, related_name='words', on_delete=models.CASCADE)
    correct_spelling = models.TextField(blank=True, null=True)
    incorrect_spelling = models.TextField(blank=True, null=True)
    difficulty = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)