from django.urls import path

from App import views

urlpatterns=[
    path("REQ", views.Scrap),
    path("REM", views.Remedy),
    path("", views.home),
    path("REMEDY", views.remedypage),
    path("Search", views.Search),
    path("About", views.About),
    path("Team", views.Team),
    path("Contact", views.Contact),
    path("CONTACT", views.CONTACT)
]