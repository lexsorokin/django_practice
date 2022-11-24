from django.db import transaction
from django.db.models import Sum, Count
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin, FormView

from app_users.forms import DepositForm, PeriodForReport
from .forms import AddGoodToCart
from app_market_place.models import Store, Goods, Cart
from app_users.models import Profile, PurchasedGoods


class StoreList(ListView):
    model = Store
    template_name = 'market_place/store_list.html'
    context_object_name = 'store_list'


class StoreGoodsDetail(DetailView):
    model = Store
    template_name = 'market_place/store_goods_detail.html'
    context_object_name = 'store'

    def get_context_data(self, **kwargs):
        context = super(StoreGoodsDetail, self).get_context_data()
        context['goods'] = Goods.objects.only('title', 'code', 'description', 'price', 'remaining_stock').filter(
            store=self.kwargs['pk'])
        return context


class AddGoodQuantityToCart(FormMixin, DetailView):
    model = Goods
    form_class = AddGoodToCart
    template_name = 'market_place/add_to_cart.html'
    context_object_name = 'good'

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        with transaction.atomic():
            reserved_good_quantity = form.cleaned_data.get('quantity')
            reserved_good = self.get_object()
            ordered_good_price_sum = reserved_good.price * reserved_good_quantity
            Cart.objects.create(
                user=self.request.user,
                good=reserved_good,
                good_quantity=reserved_good_quantity,
                ordered_good_price_sum=ordered_good_price_sum
            )
            user_profile = Profile.objects.get(user=self.request.user)
            user_profile.payment_for_cart += ordered_good_price_sum
            user_profile.save()
            reserved_good.remaining_stock -= reserved_good_quantity
            reserved_good.save()
        return HttpResponseRedirect('/market_place/stores/')


class CartDisplay(ListView):
    model = Cart
    template_name = 'market_place/cart_list.html'
    context_object_name = 'cart'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CartDisplay, self).get_context_data()
        context['cart_sum'] = 0
        for good in self.get_queryset():
            context['cart_sum'] += good.ordered_good_price_sum
        return context

    def get_queryset(self):
        queryset = self.model.objects.only('ordered_good_price_sum').filter(user=self.request.user)
        return queryset


class DepositFunds(FormView):
    form_class = DepositForm
    template_name = 'market_place/deposit.html'

    def form_valid(self, form):
        with transaction.atomic():
            deposited_funds = form.cleaned_data.get('deposit')
            user_profile = self.request.user.profile
            profile_object = Profile.objects.get(user=self.request.user)
            profile_object.balance += deposited_funds
            profile_object.save()
        return HttpResponseRedirect(f'/users/profile/{user_profile.id}/account_info/')


class PaymentForOrder(DetailView):
    model = Profile
    context_object_name = 'profile'
    template_name = 'market_place/payment.html'

    def post(self, request, *args, **kwargs):
        with transaction.atomic():
            profile = Profile.objects.get(user=request.user)
            cart = Cart.objects.select_related('good').filter(user=request.user)

            if profile.payment_for_cart >= 100000:
                profile.status = 'VIP'

            # PurchasedGoods.objects.bulk_create(
            #     [
            #         PurchasedGoods(
            #             user=request.user,
            #             good_title=purchased_good.good.title,
            #             good_obj=purchased_good.good,
            #             good_quantity=purchased_good.good_quantity,
            #             purchase_sum=purchased_good.ordered_good_price_sum
            #         )
            #         for purchased_good in cart
            #     ]
            # )

            for purchased_good in cart:
                purchase = PurchasedGoods.objects.create(
                    user=request.user,
                    good=purchased_good.good,
                    good_quantity=purchased_good.good_quantity,
                    purchase_sum=purchased_good.ordered_good_price_sum
                )
                purchase.good.purchases.add(purchase)
                purchase.good.save()

            profile.balance -= profile.payment_for_cart
            profile.payment_for_cart = 0

            profile.save()
            cart.delete()

        return HttpResponseRedirect('/market_place/stores')


class Report(View):

    def get(self, request):
        form = PeriodForReport()
        return render(request, 'market_place/report.html', {'form': form})

    def post(self, request):
        form = PeriodForReport(request.POST)
        if form.is_valid():
            start_date = form.cleaned_data.get('start_date')
            end_date = form.cleaned_data.get('end_date')
            top_purchases = Goods.objects.prefetch_related('purchases').filter(purchasedgoods__purchase_date__range=[start_date, end_date]).values('title', 'price', 'code').annotate(sum=Sum('purchases__good_quantity')).order_by('-sum')[:3]
            print(top_purchases)
            return render(request, 'market_place/report.html',
                          {'report_data': top_purchases, 'form': form, 'start_date': start_date, 'end_date': end_date})
