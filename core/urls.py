from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from django.views.i18n import JavaScriptCatalog


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dengue.urls')),
]

admin.site.site_header = 'Biliran Dengue Monitoring System'                 
admin.site.index_title = 'Dashboard'               
admin.site.site_title = 'Biliran Dengue Monitoring System'