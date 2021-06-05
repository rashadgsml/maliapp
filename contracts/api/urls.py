from django.urls import path
from .views import ContractsView, ContractDetail

app_name = 'contracts'

urlpatterns = [
    path('contracts/', ContractsView.as_view(), name='contracts'),
    path('contract-detail/<int:pk>/', ContractDetail.as_view(), name='contract-detail'),
]