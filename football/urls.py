from django.urls import path
from .views import PortugalView, EnglandView, SpainView, ItalyView, FranceView, GermanyView, LiveView

urlpatterns = [
    path('pt/', PortugalView.as_view(), name='pt'),
    path('en/', EnglandView.as_view(), name='en'),
    path('es/', SpainView.as_view(), name='es'),
    path('fr/', FranceView.as_view(), name='fr'),
    path('ge/', GermanyView.as_view(), name='ge'),
    path('it/', ItalyView.as_view(), name='it'),
    path('live/', LiveView.as_view(), name='live'),
]