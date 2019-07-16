from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView # new
urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('',TemplateView.as_view(template_name='home.html'), name='home'),
    path('accounts/', include('django.contrib.auth.urls')),  # new
path('accounts/', include('accounts.urls')), # new
]