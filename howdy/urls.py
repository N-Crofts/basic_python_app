# howdy/urls.py
from django.conf.urls import url
from howdy import views


urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^about/$', views.AboutPageView.as_view()), # Add this /about/ route
    url(r'^python/$', views.PythonWinsView.as_view()),
    url(r'^gator/$', views.GatorWinsView.as_view()),
]
