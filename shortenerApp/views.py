from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View

from shortenerApp.forms import UrlForm
from shortenerApp.models import Urls


class StatisticView(View):
    def get(self, request, id, *args, **kwargs):
        try:
            link = Urls.objects.get(pk=id)
        except:
            raise Http404
        context = {
            "id": id,
            "link": link,
        }
        return render(request, template_name="statistic.html", context=context)


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
            new_pk = new_url.pk
            new_url = "http://linkshortner.pythonanywhere.com/" + str(new_url.pk)

        context = {
            "new_url": new_url,
            'new_url_id': new_pk,
        }
        return render(request, template_name='home_post.html', context=context)
