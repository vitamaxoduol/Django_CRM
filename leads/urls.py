from django.urls import path
from .views import lead_list, lead_details, lead_update, lead_delete, lead_create

app_name = 'leads'

urlpatterns = [
    path('', lead_list, name='lead_list'),
    path('<int:pk>/', lead_details, name='lead_detail'),
    path('<int:pk>/update/', lead_update, name='lead_update'),
    path('<int:pk>/delete/', lead_delete, name='lead_delete'),
    path('create/', lead_create),
]

