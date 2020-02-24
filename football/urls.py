from django.urls import path
from .views import PortugalView

urlpatterns = [
    path('', PortugalView.as_view(), name='pt'),
]