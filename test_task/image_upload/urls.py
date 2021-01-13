from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('image_upload/', include('image_upload.urls')),
    path('upload/', views.image_upload_view),
    path('', views.image_upload_view, name='image_upload_view'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)