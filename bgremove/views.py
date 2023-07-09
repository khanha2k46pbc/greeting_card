from django.views.generic import CreateView, DetailView

from bgremove.models import UserActivity


class UploadView(CreateView):
    model = UserActivity
    fields = ["image"]
    template_name = "bgrem/index.html"


class ResultView(DetailView):
    model = UserActivity
    template_name = "bgrem/result.html"
    context_object_name = "user_activity"
