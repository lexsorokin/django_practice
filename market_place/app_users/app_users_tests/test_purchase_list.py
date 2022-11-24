from django.contrib.auth.models import User
from django.test import TestCase

from app_market_place.models import Goods, Store
from app_users.models import UserPurchaseHistory

number_of_goods = 3


class AppUsersPurchaseHistory(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user(username='username', password='password4567')
        Store.objects.create(
            title='Store',
            description='store',
            owner=user
        )
        for i in range(number_of_goods):
            Goods.objects.create(
                title=f'{i}',
                description=f'{i}',
                store=Store.objects.first(),
                price=i,
                code=i
            )

        for good_index in range(len(Goods.objects.all())):
            UserPurchaseHistory.objects.create(
                user=user,
                purchased_good=Goods.objects.all()[good_index],
                purchase_sum=Goods.objects.all()[good_index].price
            )

    def test_store_list_exists_at_correct_location_and_template(self):
        url = f'/users/profile/{User.objects.first().id}/purchase_history'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/purchase_history.html')

    def test_store_list_output_is_correct(self):
        url = f'/users/profile/{User.objects.first().id}/purchase_history'
        response = self.client.get(url)
        self.assertEqual(len(response.context['purchase_history']), number_of_goods)
