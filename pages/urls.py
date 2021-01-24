from django.urls import path

from .views import (
    HomePageView, 
    AboutPageView,
    BookPageView,
    CodingPageView,
    MusicPageView,
    PeoplePageView,
    PerspectivePageView,
    TravelPageView,
    
)

urlpatterns = [
    path('travel/', TravelPageView.as_view(), name='travel'),
    path('perspective/', PerspectivePageView.as_view(), name='perspective'),
    path('people/', PeoplePageView.as_view(), name='people'),
    path('music/', MusicPageView.as_view(), name='music'),
    path('coding/', CodingPageView.as_view(), name='coding'),
    path('book/', BookPageView.as_view(), name='book'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('', HomePageView.as_view(), name='home'),
]

