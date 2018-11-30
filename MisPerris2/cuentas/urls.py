from django.conf.urls import url, include
from . import views

app_name ='cuentas'

urlpatterns = [
    url(r'^oauth/', include('social_django.urls', namespace="social")),
    url(r'^signup/$', views.signup_view, name="signup"),
    url(r'^login/$', views.login_view, name="login"),
    url(r'^logout/$', views.logout_view, name="logout"),
   
]