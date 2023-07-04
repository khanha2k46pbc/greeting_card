from django.urls import path

from . import views

urlpatterns = [
    path("editor/", views.editor, name="editor"),
    path('', views.home, name='home'),
]