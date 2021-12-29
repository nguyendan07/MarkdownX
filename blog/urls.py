from django.urls import path

from .views import home, blog


urlpatterns = [
    path('', view=home, name='home'),
    path('blog/<slug:slug>', view=blog, name='blog')
]
