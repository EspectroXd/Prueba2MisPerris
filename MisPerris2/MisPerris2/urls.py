from django.contrib import admin
from django.conf.urls import url, include
from . import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^about/$', views.about),
    url(r'^$', views.homepage),

    #adopcion
    url(r'^FormularioAdopcion/',include('adopcion.urls', namespace='adopcion')),

]

#cada vez se configura algo de la tabla o BD
#python manage.py makemigrations
#pythons manage.py migrate

#guardar en git
#git commit -a -m "nombre commit"
#git push -u origin master