from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from accounts import models

admin.site.register(models.FileRouter)
admin.site.register(models.Router)


from main.views import IndexPageView, ChangeLanguageView, test_form,test_form1,test_video

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', test_form, name='index'),
    path('form/', test_form1, name="form"),
    path('video/', test_video, name="video"),

    path('i18n/', include('django.conf.urls.i18n')),
    path('language/', ChangeLanguageView.as_view(), name='change_language'),

    path('accounts/', include('accounts.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
