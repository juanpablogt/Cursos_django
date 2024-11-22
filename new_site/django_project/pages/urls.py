from django.urls import path
from .views import HomePageView, My_codesPageView,ContactPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('my_codes/', My_codesPageView.as_view(), name='my_codes'),
    path('contact/', ContactPageView.as_view(), name='contact'),
]