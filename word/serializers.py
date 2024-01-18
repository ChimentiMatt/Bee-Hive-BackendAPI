from rest_framework import serializers
from .models import Word

from account.serializers import UserSerializer

class WordSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = Word
        fields = ('id', 'correct_spelling', 'incorrect_spelling', 'difficulty', 'created_at', 'created_by',)