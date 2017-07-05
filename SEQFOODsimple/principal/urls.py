from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views



urlpatterns=[
	url(r'^$', views.index, name='index'),
	url(r'^busqueda/$', views.gestionBusqueda, name="gestionBusqueda"),
	url(r'^busqueda/(?P<pk>[a-z0-9]+)/$', views.VistaDetalleAlimento.as_view(), name="detalle_alimento"),
	url(r'^busqueda_avanzada/$', views.busquedaAvanzada, name="busquedaAvanzada"),
	url(r'^login/$', auth_views.login, name='login'),
	url(r'^logout/$', auth_views.logout, {'template_name': 'registration/logout.html'}, name='logout'),
]