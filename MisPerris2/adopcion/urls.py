from django.conf.urls import url
from . import views

app_name='adopcion'

urlpatterns = [
    url(r'^adoptadosList/$', views.Formulario_adopcion_Listar, name="adoptadosListar"),
    url(r'^adoptadosCreate/$', views.Formulario_adopcion_Crear, name="adoptadosCrear"),

    url(r'^rescatadosList/$', views.Formulario_rescatados_Listar, name="rescatadosListar"),
    #url(r'(?P<correo>[\w-]+)/',views.Formulario_detalles, name="Detalle"),
]
