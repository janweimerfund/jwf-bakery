from django.views import generic
from bakery import views
from . import models


MAILING_ADDRESS = [
    'c/o Dr. Sanford Weimer',
    '517 E. Wilson, Ste. 105,',
    'Glendale, CA 91206'
]


class IndexView(views.BuildableTemplateView):
    build_path = "index.html"
    template_name = "jwf/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title': "JWF",
            # "navs": models.Page.objects.values('title', 'view'),
            "address": MAILING_ADDRESS
        })
        context['navs'] = [
            {'view': 'about', 'title': 'About'},
            {'view': 'events', 'title': 'Events'},
            {'view': 'contact', 'title': 'Contact'},
        ]
        return context


class EventsView(IndexView):
    build_path = "events/index.html"
    template_name = "jwf/events.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['events'] = []
        context['events'] = models.Event.objects.values('date', 'name', 'description')
        return context


# class EventDetail(IndexView):
#     template_name = "jwf/events.html"


class AboutView(IndexView):
    build_path = "about/index.html"
    template_name = "jwf/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['articles'] = models.Article.objects.values('title', 'cite')
        return context


class ContactView(IndexView):
    build_path = "contact/index.html"
    template_name = "jwf/contact.html"
