from django.test import TestCase

from app_users.forms import RegistrationForm
from app_users.models import Profile

URL = '/users/registration/'


class AppUsersRegistrationViewTests(TestCase):

    def test_user_registration_exists_at_correct_location_and_template(self):
        response = self.client.get(URL)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/registration.html')

    def test_model_form_is_valid(self):
        reg_form = RegistrationForm(
            {
                'username': 'a',
                'first_name': 'b',
                'last_name': 'b',
                'email': 'ccc@cccc.com',
                'phone': '1111111111',
                'address': 'F str, 1',
                'password1': 'username4523',
                'password2': 'username4523'
            }
        )
        self.assertTrue(reg_form.is_valid())

    def test_user_profile_creation(self):
        user_profile_data = {
                'username': 'a',
                'first_name': 'b',
                'last_name': 'b',
                'email': 'ccc@cccc.com',
                'phone': '1111111111',
                'address': 'F str, 1',
                'password1': 'username4523',
                'password2': 'username4523'
            }
        user_profile = self.client.post(
            path=URL,
            data=user_profile_data,
            follow=True
        )
        self.assertEqual(user_profile_data['username'], Profile.objects.first().user.username)
        self.assertEqual(user_profile_data['first_name'], Profile.objects.first().first_name)
        self.assertEqual(user_profile_data['last_name'], Profile.objects.first().last_name)
        self.assertRedirects(user_profile, expected_url='/market_place/stores/')

