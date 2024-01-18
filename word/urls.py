from django.urls import path

from . import api

urlpatterns = [
    path('', api.word_list, name='word_list'),
    path('user_words', api.users_words, name='user_words'),
    path('create', api.word_create, name='word_create'),
    path('<uuid:pk>/delete_word', api.delete_word, name='delete_word'),
]
