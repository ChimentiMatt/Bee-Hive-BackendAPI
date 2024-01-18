from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .serializers import WordSerializer
from .models import Word
from .forms import PostForm

@api_view(['GET'])
def word_list(request):
    words = Word.objects.all()
    serializer = WordSerializer(words, many=True)
    return JsonResponse( {'data': serializer.data} )

@api_view(['GET'])
def users_words(request):
    current_user = request.user
    user_words = Word.objects.filter(created_by=current_user)
    serializer = WordSerializer(user_words, many=True)

    return JsonResponse( {'data': serializer.data} )

@api_view(['POST'])
def word_create(request):
    form = PostForm(request.data)

    if (form.is_valid):
        word = form.save(commit=False)
        word.created_by = request.user
        # post.correct_spelling = request.correct_spelling
        # post.incorrect_spelling = request.incorrect_spelling
        word.save()

        serializer = WordSerializer(word)

        return JsonResponse(serializer.data, safe=False)
    else:
        return JsonResponse({'error': 'unable to process request'})
    
@api_view(['DELETE'])
def delete_word(request, pk):
    word = Word.objects.filter(created_by=request.user).get(pk=pk)
    word.delete()

    return JsonResponse( {'message': 'word deleted'} )

