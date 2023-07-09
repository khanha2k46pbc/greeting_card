from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

from bgremove.views import UploadView, ResultView
from main.views import index_page_view, ChangeLanguageView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', index_page_view, name='index'),

    path('i18n/', include('django.conf.urls.i18n')),
    path('language/', ChangeLanguageView.as_view(), name='change_language'),

    path('accounts/', include('accounts.urls')),
    path("bgrem",  UploadView.as_view(), name="background-remove"),
    path("result/<slug:slug>/", ResultView.as_view(), name="result"),
    path('bgremove/', include('bgremove.urls', namespace='bgremove')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
