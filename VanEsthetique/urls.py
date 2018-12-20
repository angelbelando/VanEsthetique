"""VanEsthetique URL Configuration
"""
from django.urls import include, path, re_path
from django.views.generic import TemplateView
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import ugettext as _

from django.contrib import admin
from soins  import views
urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^i18n/', include('django.conf.urls.i18n')), 
    # path('', views.Index.as_view(), name='index'),
    # path('soins/', include('soins.urls', namespace='soins')),
    # path('contact/', TemplateView.as_view(template_name='contact.html'), name='contact'),
     
]
urlpatterns += i18n_patterns(
    path('', views.Index.as_view(), name='index'),
    path('soins/', include('soins.urls', namespace='soins')),
    path('contact/', TemplateView.as_view(template_name='contact.html'), name='contact'),
    prefix_default_language=True,
)
