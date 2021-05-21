
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from home import views

app_name = "home"

router = DefaultRouter()
router.register('v1/clients', views.ClientViewSet)


urlpatterns = [
    path('index', views.Index.as_view(), name = "index"),
    path('list_client/', views.ListClientView.as_view(), name="list_client"),
    path('pokelist/', views.PokeView.as_view(), name="pokelist"),
    path('ws/clients/', views.wsClient, name="wsclients"),
    path('ws/views_clients/', views.ViewWsClient.as_view(), name="views_ws_client"),

    ### v1
    path('v1/client_list/', views.client_list, name="client_list"),
    path('v1/client_detail/<int:pk>/', views.client_update, name="client_detail"),

    ### v2
    path('v2/client_list/', views.ClientListAPIView.as_view(), name="list_client2"),
    path('v2/detail_client/<int:pk>/', views.DetailClientAPIView.as_view(), name="detail_client2"),

    ### v3
    path('v3/clients/', views.ClientListCreate.as_view(), name="clients"),
    path('v3/clients/<int:pk>/', views.ClientRetrieveUpdateDestroy.as_view(), name="clients_rud"),
]

urlpatterns += router.urls