from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.views import View
from nirn.models import Nirnroot, Nirn, NirnFile
import json


def home(request):
    context = {
        'title': 'Nirn',
        "nirnroots": Nirnroot.objects.all(),
    }
    html = render_to_string('home.html', context)
    return HttpResponse(html)


class NirnrootView(View):
    def post(self, request, *args, **kwargs):
        slug = request.POST.get('slug')
        passphrase = request.POST.get('passphrase')
        name = request.POST.get('name')
        nirnroot = Nirnroot.objects.create(
            slug=slug,
            passphrase=passphrase,
            name=name,
        )
        context = {
            'id': nirnroot.id,
            'slug': nirnroot.slug,
            'passphrase': nirnroot.passphrase,
            'name': nirnroot.name,
        }
        return render(request, 'nirnroots.html', context)
    
    def delete(self, request, *args, **kwargs):
        slug = request.POST.get('slug')
        passphrase = request.POST.get('passphrase')
        nirnroot = Nirnroot.objects.get(slug=slug, passphrase=passphrase)
        nirnroot.delete()
        return HttpResponse(status=204)
