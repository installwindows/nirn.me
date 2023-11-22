from django.urls import path
import views


urlpatterns = [
    path("", views.home, name='homepage'),
    path("nirn", views.NirnView.as_view(), name='nirn'),
]
