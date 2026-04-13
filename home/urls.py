from django.urls import path
from home import views


urlpatterns = [
    path('', views.home,name="home" ),
    path("contact/", views.contact, name="contact"),
    path("about/", views.about, name="about"),
    path("service/", views.service, name="service"),
    path("project/", views.project, name="project"),
    # path("dog-upload/", views.uploadDog, name="dog-upload")
]

