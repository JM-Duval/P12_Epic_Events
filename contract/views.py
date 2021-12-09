from rest_framework import viewsets
from contract.models import Contract
from contract.serializers import ContractSerializer
from client.models import Client
from client.serializers import ClientSerializer
from rest_framework.response import Response
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from contract.permissions import IsSalerContact, IsManager


class ContractViewset(viewsets.ModelViewSet):

    permission_classes = [ IsSalerContact | IsManager ]
    serializer_class = ContractSerializer
    queryset = Contract.objects.all()
    http_method_names = ['get', 'post', 'delete', 'put']
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ("client__first_name", "client__last_name", 
        "client__email", "date_created", "amount")
    
        
    def get_queryset(self):
        return Contract.objects.all()

    def list(self, request):
        id_user = request.user.id
        contract = Contract.objects.filter(sales_contact=id_user)
        serializer = ContractSerializer(contract, many=True)
        return Response(serializer.data)