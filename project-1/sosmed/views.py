from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView, RedirectView, View
# Create your views here.
from .models import instagram
from .forms import instagramForm


class sosmedSubList:

    def get_list_data(self, get_request):
        if len(get_request) == 0:
            subList = instagram.objects.all()
        elif get_request.__contains__('sosial_media_filter'):
            subList = instagram.objects.filter(
                sosial_media=get_request['sosial_media_filter'])
        else:
            subList = instagram.objects.none()

        return subList


class sosmedListView(sosmedSubList, TemplateView):
    template_name = 'sosmed/list.html'

    def get_context_data(self, *args, **kwargs):
        # akun = instagram.objects.all()
        listAkun = self.get_list_data(self.request.GET)
        listContent = instagram.objects.values_list(
            'sosial_media', flat=True).distinct()
        print(listContent)
        context = {
            'page_title': 'Social Media',
            'akun': listAkun,
            'content': listContent,
        }
        return context


class sosmedDeleteView(RedirectView):
    pattern_name = 'sosmed:list'
    permanent = False
    query_string = False

    def get_redirect_url(self, *args, **kwargs):
        delete_id = kwargs['delete_id']
        print(delete_id)
        instagram.objects.filter(id=delete_id).delete()
        return super().get_redirect_url()


class sosmedFormView(View):
    template_name = 'sosmed/create.html'
    form = instagramForm()
    mode = None
    context = {}

    def get(self, *args, **kwargs):
        if self.mode == 'update':
            akunUpdate = instagram.objects.get(id=kwargs['update_id'])
            data = akunUpdate.__dict__
            self.form = instagramForm(initial=data, instance=akunUpdate)

        self.context = {
            'page_title': 'Update Akun',
            'akun_form': self.form,
        }
        return render(self.request, self.template_name, self.context)

    def post(self, *args, **kwargs):
        if kwargs.__contains__('update_id'):
            akunUpdate = instagram.objects.get(id=kwargs['update_id'])
            self.form = instagramForm(self.request.POST, instance=akunUpdate)

        else:
            self.form = instagramForm(self.request.POST)

        if self.form.is_valid():
            self.form.save()

        return redirect('sosmed:list')
