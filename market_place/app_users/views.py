from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect, render
from django.views.generic import DetailView, ListView
from app_users.forms import RegistrationForm
from app_users.models import Profile, PurchasedGoods


class Login(LoginView):
    template_name = 'user/login.html'


class Logout(LogoutView):
    next_page = '/market_place/stores/'


def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            phone = form.cleaned_data.get('phone')
            address = form.cleaned_data.get('address')
            Profile.objects.create(
                user=user,
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone,
                address=address,
                balance=0
            )
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password2')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/market_place/stores/')
    else:
        form = RegistrationForm()
    return render(request, template_name='user/registration.html', context={'form': form})


class AccountInfo(DetailView):
    model = Profile
    template_name = 'user/profile_detail.html'
    context_object_name = 'profile'


class PurchaseHistory(ListView):
    model = PurchasedGoods
    template_name = 'user/user_purchase_history.html'
    context_object_name = 'purchase_history'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PurchaseHistory, self).get_context_data()
        purchases = self.get_queryset()
        context['overall_purchase_sum'] = 0
        for purchase in purchases:
            context['overall_purchase_sum'] += purchase.purchase_sum
        return context

    def get_queryset(self):
        queryset = self.model.objects.select_related('good').filter(user=self.request.user)
        return queryset