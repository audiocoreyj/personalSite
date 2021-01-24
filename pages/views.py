from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'index.html'
    
class AboutPageView(TemplateView):
    template_name = 'about.html'
    
class BookPageView(TemplateView):
    template_name = 'books.html'
    
class CodingPageView(TemplateView):
    template_name = 'coding.html'
    
class MusicPageView(TemplateView):
    template_name = 'music.html'
    
class PeoplePageView(TemplateView):
    template_name = 'people.html'
    
class PerspectivePageView(TemplateView):
    template_name = 'perspective.html'
    
class TravelPageView(TemplateView):
    template_name = 'travel.html'
    
    
    
    