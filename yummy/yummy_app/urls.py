from django.template.defaulttags import url
from django.urls import path
from django.views.generic import RedirectView

from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('details/<int:id>/', details, name='details'),
    path('category/<int:id>/', category, name='category'),
    path('aboutus/', aboutus, name='aboutus'),
    path('search/', search, name='search'),
    path('registration/', registration, name="registration"),
    path('cart/', cart, name='cart'),
    path('cart/add-product/<int:id>', add, name='add'),
    path('cart/remove-product/<int:id>', remove, name='remove'),
    path('cart/remove-all', remove_all, name='remove-all'),
    path('profile/', profile, name='profile'),
    path('buy/', buy, name='buy'),
    path('thanks/', thanks, name='thanks')
]
