from django.urls import path
from django.views.generic import TemplateView

app_name = 'uppy'

urlpatterns = [
    path('', TemplateView.as_view(template_name='uppy/index.html')),
]
