from django.conf.urls import url
from . import views
from .views import Formulario_adopcion_crear

urlpatterns = [
    url(r'^$', views.Formulario_adopcion_Listar),
    url(r'^Nuevo$', views.Formulario_adopcion_crear(), name='new'),
]
