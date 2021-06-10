from django.contrib import admin
from django.urls import path, include
# from django.conf.urls.static import static
# from django.conf import settings


urlpatterns = [
    path('', include('photo.urls')),
    path('accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls),
]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#python manage.py shell
#from config import urls
#urls.urlpatterns
#   [<URLResolver <module 'photo.urls' from 'C:\\Users\\ddukf\\source\\dstagram\\photo\\urls.py'> (photo:photo) ''>, <URLResolver <URLPattern list> (admin:admin) 'admin/'>, <URLPattern '^media/(?P<path>.*)$'>]
