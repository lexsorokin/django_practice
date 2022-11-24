from django.contrib.auth.models import User
from django.test import TestCase
from app_market_place.models import Store


class AppMarketPlaceTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user(username='username', password='password4567')
        Store.objects.create(
            title='Store',
            description='store',
            owner=user
        )

    def test_store_detail_exists_at_correct_location_and_template(self):
        url = f'/market_place/store/{Store.objects.first().id}/'
        response = self.client.get(url)
        print(Store.objects.first())
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'market_place/store_goods_detail.html')

