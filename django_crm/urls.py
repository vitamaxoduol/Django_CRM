from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('leads/', include('leads.urls')),
    re_path(r'^$', RedirectView.as_view(url='/leads/', permanent=True)),
]
