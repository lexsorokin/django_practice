from django.contrib.auth.models import User
from django.test import TestCase

from app_market_place.models import Store

number_of_stores = 10
url = f'/market_place/stores/'


class AppMarketPlaceTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user(username='username', password='password4567')
        for i in range(number_of_stores):
            Store.objects.create(
                title=f'Store{i}',
                description=f'store{i}',
                owner=user

            )

    def test_user_profile_detail_exists_at_correct_location_and_template(self):
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'market_place/store_list.html')

    def test_purchase_history_output_is_correct(self):
        response = self.client.get(url)
        self.assertEqual(len(response.context['store_list']), number_of_stores)
