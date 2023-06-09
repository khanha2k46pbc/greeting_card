from django.urls import path

from .views import ResultView, UploadView

app_name = "bgremove"

urlpatterns = [
    path("", UploadView.as_view(), name="background-remove"),
    path("result/<slug:slug>/", ResultView.as_view(), name="result"),
]
