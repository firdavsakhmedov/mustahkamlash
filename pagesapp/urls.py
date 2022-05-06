from django.urls import path
from .views import AboutPageView, HomePageView, TelegramPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('tg/', TelegramPageView.as_view(), name='telegram'),
    path('about/', AboutPageView.as_view(), name='about'),
]
