from django.core.paginator import Paginator
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View

from shortenerApp.forms import UrlForm
from shortenerApp.models import Urls


class AnalysisView(View):
    def post(self, request, *args, **kwargs):
        context = {

        }
        return render(request, template_name="analysis.html", context=context)


class LinkView(View):
    def get(self, request, *args, **kwargs):
        url = Urls.objects.get(pk=kwargs["store_id"])
        url.click_count += 1
        url.save()
        response = redirect(url.url)
        return response


class HomeView(View):
    def get(self, request, *args, **kwargs):
        form = UrlForm()
        recent_forms = Urls.objects.all()
        context = {
            "form": form,
            'resent_form': recent_forms,
        }
        return render(request, template_name='home.html', context=context)

    def post(self, request, *args, **kwargs):
        post_form = UrlForm(request.POST)
        if post_form.is_valid():
            new_url = Urls.objects.get_or_create(url=post_form.cleaned_data['url'])
            try:
                new_url.save()
            except:
                new_url = new_url[0]
            new_url = "http://127.0.0.1:8000/" + str(new_url.pk)

        context = {
            "new_url": new_url,
        }
        return render(request, template_name='home_post.html', context=context)
