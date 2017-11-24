from django.conf.urls import url
from recepti_app.views import receptiView,problemListView,traveList,receptDetail

app_name = 'recepti_app'

urlpatterns = [
    url(r'^$',receptiView.as_view(),name='recepti_view'),
    url(r'^problemi/$',problemListView.as_view(),name='problemlist'),
    url(r'^detalji/(?P<pk>\d+)/$',traveList.as_view(),name='detail'),
    url(r'^recept/(?P<pk>\d+)/$',receptDetail.as_view(),name='recept'),
]
