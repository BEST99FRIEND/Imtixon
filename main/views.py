from django.shortcuts import render
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'home.html'
    def get(self, request):
        return render(request, 'main/index.html')
    
class AboutView(TemplateView):
    template_name = 'about.html'
    def get(self, request):
        return render(request, 'main/about.html')
    
class DealsView(TemplateView):
    template_name = 'deals.html'
    def get(self, request):
        return render(request, 'main/deals.html')
    
class ReservationView(TemplateView):
    template_name = 'reservation.html'
    def get(self, request):
        return render(request, 'main/reservation.html')
    
class CountryDetailView(TemplateView):
    template_name = 'country_detail.html'
    def get(self, request, pk):
        from main.models import Countries
        country = Countries.objects.get(pk=pk)
        return render(request, 'main/country_detail.html', {'country': country})