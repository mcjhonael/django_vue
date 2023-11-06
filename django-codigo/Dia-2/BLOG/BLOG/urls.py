from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.contrib.staticfiles.urls import static,staticfiles_urlpatterns



#ya tenemos 2 rtas una para el admin y otra ruta de nuestra app que hemos incluido
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('core.urls'))
]

#!acceder a la arpeta donde se encuentran los archvos media
urlpatterns +=staticfiles_urlpatterns()
urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)