from django.contrib import admin
from django.conf.urls import url, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^cuentas/', include('cuentas.urls')),
    url(r'^formularioAdopcion/', include('adopcion.urls')),
    url(r'^about/$', views.about),
    url(r'^Home/$', views.Home, name="Home"),
    url(r'^$', views.homepage, name="homepage"),
    #url(r'^', include('django.contrib.auth.urls')),
    #url(r'^oauth/', include('social_django.urls',namespace="social")),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



#cada vez se configura algo de la tabla o BD
#python manage.py makemigrations
#pythons manage.py migrate

#guardar en git
#git commit -a -m "nombre commit"
#git push -u origin master