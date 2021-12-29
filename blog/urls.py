from django.urls import path

from .views import home, blog, create, preview


urlpatterns = [
    path('', view=home, name='home'),
    path('create', view=create, name='create'),
    path('preview', view=preview, name='preview'),
    path('blog/<slug:slug>', view=blog, name='blog')
]
