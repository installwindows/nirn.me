from django.urls import path
from django.http import HttpResponse
from django.template.loader import render_to_string
DEBUG = True
SECRET_KEY = 'secret'

ROOT_URLCONF = __name__

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            'templates/'
        ],
    },
]

def home(request):
    context = {
        'title': 'Hello World',
        'content': 'This is the content of the page.',
    }
    html = render_to_string('home.html', context)
    return HttpResponse(html)

urlpatterns = [
    path("", home, name='homepage'),
]
