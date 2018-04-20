from django import urls
from django.contrib import admin
from . import views

app_name = 'jwf'
urlpatterns = [
    urls.path('admin/', admin.site.urls),
    urls.path('', views.IndexView.as_view(), name="index"),
    urls.path('about/', views.AboutView.as_view(), name="about"),
    urls.path('events/', views.EventsView.as_view(), name="events"),
    urls.path('contact/', views.ContactView.as_view(), name="contact")
]
