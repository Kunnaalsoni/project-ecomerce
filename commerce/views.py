from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from commerce.models import Product
from django.utils import timezone
from django.conf import settings
from django.urls import reverse_lazy
from commerce.forms import UserCreateForm
from django.contrib.auth import authenticate, login as lg, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Cart, Address
from django.contrib.auth.models import User
# Create your views here.
class ProductListView(ListView):
    template_name = 'commerce/productlist.html'
    model = Product

class ProductDetailView(DetailView):
    model = Product
    template_name = 'commerce/productdetail.html'

    def post(self, request, slug, *args, **kwargs):
        if request.POST.get('quantity')!= None :
            username = request.user
            item = get_object_or_404(Product, slug = slug)
            quantity = request.POST.get('quantity')
            x = Cart(user = username, item = item, quantity = quantity)
            x.save()
            return redirect('commerce:address')
        return render(request, 'commerce/cart.html')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class UserCreateView(CreateView):
    form_class = UserCreateForm
    template_name = 'commerce/signup.html'
    success_url = reverse_lazy('commerce:productlist')



def login(request):
    username1 = request.POST.get('username')
    password1 = request.POST.get('password')
    user = authenticate(request, username=username1, password=password1)
    if user is not None:
        print("logged in")
        lg(request, user)
        # Redirect to a success page.
        return render(request, 'index.html')
    else:
        # Return an 'invalid login' error message
        pass
    return render(request, 'commerce/login.html')

def logout_view(request):
    logout_message = "You have been successfully logged out"
    logout(request)
    return render(request, 'commerce/login.html', {'data': logout_message})

def address(request):
    if request.POST.get('address-line') is not None:
        username = request.user
        address_line = request.POST.get('address-line')
        mobile_number = request.POST.get('mobile-number')

        x = Address(user= username, address_line = address_line, mobile_number = mobile_number)
        x.save()
    cart_data = Cart.objects.filter(user=request.user)
    return render(request, 'commerce/address.html' , {'data': cart_data})
