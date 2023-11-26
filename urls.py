from django.urls import path
import views


urlpatterns = [
    path("", views.home, name='homepage'),
    path("nirnroot", views.NirnrootView.as_view(), name='nirnroot'),
]
