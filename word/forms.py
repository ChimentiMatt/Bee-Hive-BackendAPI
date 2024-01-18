from django.forms import ModelForm

from .models import Word

class PostForm(ModelForm):
    class Meta:
        model = Word
        fields = ('correct_spelling', 'incorrect_spelling')