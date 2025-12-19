from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.HomeView.as_view(), name='home'),
    path('about/',views.AboutView.as_view(), name='about'),
    path('deals/',views.DealsView.as_view(), name='deals'),
    path('reservation/',views.ReservationView.as_view(), name='reservation'),
]
