from django.contrib.auth.models import User
from django.test import TestCase
from app_users.models import Profile


class AppUsersProfileViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user = User.objects.create_user(username='user', password='userman0912')
        Profile.objects.create(
            user=test_user,
            first_name='first',
            last_name='last',
            email='lalala@lalala.com',
            phone=1111111111,
            address='Lala str, 23'
        )

    def test_user_profile_detail_exists_at_correct_location_and_template(self):
        profile = Profile.objects.first()
        url = f'/users/profile/{profile.id}/account_info/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/profile_detail.html')





