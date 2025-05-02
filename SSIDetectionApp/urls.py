from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from .login import *
from django.conf import settings
from django.conf.urls.static import static
from SSIDetectionApp.settings import *


urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('', index),
    path('nurse/', include('Nurse.urls')),
    path('junior_doctor/', include('JrDoctor.urls')),
    path('senior_doctor/', include('SrDoctor.urls')),
    path('', TemplateView.as_view(template_name='frontend/index.html')),
]

urlpatterns += static(settings.STATIC_URL, document_root=os.path.join(settings.BASE_DIR, 'static/static'))