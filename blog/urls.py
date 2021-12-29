from django.urls import path

from .views import home, blog, create


urlpatterns = [
    path('', view=home, name='home'),
    path("create", view=create, name="create"),
    path('blog/<slug:slug>', view=blog, name='blog')
]
