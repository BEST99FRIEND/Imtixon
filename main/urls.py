from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('',views.HomeView.as_view(), name='home'),
    path('login/', LoginView.as_view(template_name='main/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('about/',views.AboutView.as_view(), name='about'),
    path('deals/',views.DealsView.as_view(), name='deals'),
    path('reservation/',views.ReservationView.as_view(), name='reservation'),
]
