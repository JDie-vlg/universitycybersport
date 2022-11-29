from django.urls import path, re_path
from django.contrib.auth.views import LogoutView

from .views import *

urlpatterns = [
    path('servers/', ServerListView.as_view(), name='servers'),
    path('servers/<slug:slug>/', ServerDetailView.as_view(), name='servers_detail'),
    path('servers_add/', AddServer.as_view(), name='server_add'),
    path('server_start/<int:pk>/', StartServer.as_view(), name='server_start'),
    path('server_stop/<int:pk>/', StopServer.as_view(), name='server_stop'),
    # path('csservers/add', ServerDetailView, name='server_details'),
    # path('csservers/add', ServerDetailView, name='server_debug'),
    path('take_map/<int:pk>/', TakeMap.as_view(), name='take_map'),
]