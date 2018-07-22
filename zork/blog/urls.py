from django.conf.urls import url
from . import views

urlpatterns = [
    #не обязательно именованный паратметр, можно и так, передастся 1-ым параметром в функцию home
    #у меня там уже дефолтное page_number = 1
    url(r"^$",views.home,name='home'),
    url(r"^contact/$",views.contact,name='contact'),
    url(r"^create/$",views.create,name='create'),
    url(r"^detail/(?P<pk>\d+)/$",views.detail,name='detail'),
    url(r"^delete/(?P<pk>\d+)/$",views.delete,name='delete'),
    url(r"^edit/(?P<pk>\d+)/$",views.edit,name='edit'),
    url(r'^search/',views.search,name='search'),

]
