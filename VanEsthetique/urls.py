"""VanEsthetique URL Configuration
"""
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path, re_path
from django.conf.urls import url
from django.views.generic import TemplateView
# from django.conf.urls.i18n import i18n_patterns
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls
from wagtail.core import urls as wagtail_urls
from django.utils.translation import ugettext as _

from django.contrib import admin
from soins  import views
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('soins/', include('soins.urls', namespace='soins')),
    path('contact/', TemplateView.as_view(template_name='contact.html'), name='contact'),
    re_path(r'^i18n/', include('django.conf.urls.i18n')), 
    
#wagtail
  
    re_path(r'^soins-admin/', admin.site.urls),
    re_path(r'^documents/', include(wagtaildocs_urls)),
    re_path(r'', include(wagtail_urls)),
    re_path(r'^cms-admin/', include(wagtailadmin_urls)),

    path('jet/', include('jet.urls', 'jet')),
]
# urlpatterns += i18n_patterns(
#     path('', views.Index.as_view(), name='index'),
#     path('soins/', include('soins.urls', namespace='soins')),
#     path('contact/', TemplateView.as_view(template_name='contact.html'), name='contact'),
#     prefix_default_language=False,
# )

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)