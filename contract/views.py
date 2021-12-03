from rest_framework import viewsets
from contract.models import Contract
from contract.serializers import ContractSerializer
from client.models import Client
from client.serializers import ClientSerializer
from rest_framework.response import Response
from django_filters import rest_framework as filters


class ContractViewset(viewsets.ModelViewSet):

    serializer_class = ContractSerializer

    queryset = Contract.objects.all()
    http_method_names = ['get', 'post', 'delete', 'put']
    filterset_fields = ("client__first_name", "client__last_name", "client__email", "date_created", "amount")
    filter_backends = (filters.DjangoFilterBackend,)

    def list(self, request):
        queryset = Contract.objects.all()
        serializer = ContractSerializer(queryset, many=True)
        return Response(serializer.data)
     

    """
        
        def get_id_client_with_first_name(self, first_name):
            queryset = Client.objects.filter(first_name=first_name)
            serializer = ClientSerializer(queryset, many = True)
            id_client = serializer.data[0]['id']
            return id_client
    
        def get_id_client_with_email(self, email):
            queryset = Client.objects.filter(email=email)
            serializer = ClientSerializer(queryset, many=True)
            id_client = serializer.data[0]['id']
            return id_client
    
        def get_queryset(self):
    
    
            first_name = self.request.query_params.get('first_name') # about client
            email = self.request.query_params.get('email') # about client
            date = self.request.query_params.get('date')
            amount = self.request.query_params.get('amount')
    
            if first_name is not None:
                id_client = self.get_id_client_with_first_name(first_name)
                return Contract.objects.filter(client=id_client)
            elif email is not None:
                id_client = self.get_id_client_with_email(email)     
                return Contract.objects.filter(client=id_client)
            elif date is not None:
                return Contract.objects.filter(date_created=date)
            elif amount is not None:
                return Contract.objects.filter(amount=amount)
            else:
                return Contract.objects.all()
    """