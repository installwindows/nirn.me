from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from nirn.models import Nirn, NirnFile
import json


def home(request):
    context = {
        'title': 'Nirn',
        "nirns": Nirn.objects.all(),
    }
    html = render_to_string('home.html', context)
    return HttpResponse(html)


class NirnView(View):
    def post(self, request, *args, **kwargs):
        secret_key = request.POST.get('secret_key')
        name = request.POST.get('name')
        nirn = Nirn.objects.create(
            secret_key=secret_key,
            name=name,
        )
        data = {
            'id': nirn.id,
            'secret_key': nirn.secret_key,
            'name': nirn.name,
        }
        return JsonResponse(data)
