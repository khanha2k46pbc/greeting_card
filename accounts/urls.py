from django.urls import path

from . import views

urlpatterns = [
    path("login/", views.login, name="login"),
    path("register/", views.register, name="register"),
    path("setting/<int:user_id>/", views.setting, name="setting"),
    path("uploaded_images/<int:user_id>/", views.uploaded_images, name="uploaded_images"),
    path("stored_images/<int:user_id>/", views.stored_images, name="stored_images"),
    path("upload/<int:user_id>/", views.upload, name="upload"),
]