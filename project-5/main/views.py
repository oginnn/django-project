from django.views.generic import TemplateView, ListView, DetailView
from django.contrib import messages

from .models import Certificate, ReportingResult

# Create your views here.
class index_view(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        reporting_results = ReportingResult.objects.filter(is_active=True)

        context['reporting_results'] = reporting_results

        return context
    
    success_url = "/"

    def form_valid(self, form):
        form.save()
        messages.success(
            self.request, 'Terima Kasih, Akan Saya Hubungi Segera')
        return super().form_valid(form)
    
class certificates_view(ListView):
    model = Certificate
    template_name = 'main/certificate.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        certificates = Certificate.objects.filter(is_active=True)

        context['certificates'] = certificates

        return context
    
class reporting_view(ListView):
    model = ReportingResult
    template_name = 'main/reporting.html'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)

        all_reporting = ReportingResult.objects.filter(is_active=True)

        context['reporting'] = all_reporting

        return context
    
class reporting_result_view(DetailView):
    model = ReportingResult
    template_name = "main/reporting-detail.html"