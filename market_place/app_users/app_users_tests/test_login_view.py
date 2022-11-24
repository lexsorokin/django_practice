from django.contrib.auth.models import User
from django.test import TestCase

URL = '/users/login/'


class AppUsersLoginViewTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(username='test',
                                 password='testpassword8374')

    def test_login_view_exists_at_correct_location_and_template(self):
        response = self.client.get(URL)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/login.html')

    def test_user_logged_in(self):
        logged_in = self.client.login(username='test',
                                      password='testpassword8374')
        self.assertTrue(logged_in)

    def test_user_is_not_logged_in(self):
        logged_in = self.client.login(username='test',
                                      password='testpassword83')
        self.assertFalse(logged_in)

    def test_redirect_is_correct(self):
        login_data = {
            'username': 'test',
            'password': 'testpassword8374'
        }
        login_user = self.client.post(path='/users/login/',
                                      data=login_data,
                                      follow=True)
        self.assertRedirects(login_user, expected_url='/market_place/stores/')


