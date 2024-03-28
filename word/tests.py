from django.test import TestCase
from word.models import Word
from account.models import User

class WordTestCase(TestCase):
    def setUp(self):
        user_1 = User.objects.create(id=1, email='na@gmail.com', name='test_user', avatar='', is_superuser=False, is_staff=False, date_joined='2001-01-01 00:00:00')
        Word.objects.create(id=1, created_by=user_1, correct_spelling='Apple', incorrect_spelling="apl", difficulty='easy', created_at='2001-01-01 00:00:00')

    def test_two_different_spellings(self):
        '''See if words incorrectly matches'''
        apple = Word.objects.get(correct_spelling='Apple')
        self.assertEqual(apple.correct_spelling, 'Apple')
        self.assertEqual(apple.incorrect_spelling, 'apl')

        self.assertEqual(apple.incorrect_spelling != apple.correct_spelling, True)

    def authorization_needed_to_post(self):
        '''Make sure a 401 is thrown when trying to post a word without authorization'''
        data = {
            "correct_spelling": 'word',
            "incorrect_spelling": 'wrd'
        }
        response = self.client.post('/api/words/create', data)
        self.assertEqual(response.status_code, 401)

    def able_to_post_when_authorized(self):
        '''Make sure a 401 is thrown when trying to post a word without authorization'''
        self.client.force_authentication(user=self.user)
        data = {
            "correct_spelling": 'word',
            "incorrect_spelling": 'wrd'
        }
        response = self.client.post('/api/words/create', data)

        self.assertEqual(response.status_code, 200)
