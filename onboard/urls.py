from django.conf.urls import include, url
from .views import OnboardView, NextStepsView


urlpatterns = [
    url(r'^$', OnboardView.as_view(), name='get-started'),
    url(r'^next-steps$', NextStepsView.as_view(), name='next-steps'),
]