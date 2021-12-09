from django.shortcuts import render
from rest_framework import viewsets 
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from client.permissions import IsSalerContact, IsTechnicianEventContact, IsManager
from client.serializers import UserSerializer, RegisterSerializer, ClientSerializer
from client.models import Client, User
from event.models import Event
from rest_framework.decorators import permission_classes
from django_filters.rest_framework import DjangoFilterBackend


class ClientViewset(viewsets.ModelViewSet):

    permission_classes = [ IsSalerContact  | IsTechnicianEventContact | IsManager ]
    serializer_class = ClientSerializer
    queryset = Client.objects.all()
    http_method_names = ['get', 'post', 'delete', 'put']
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ("first_name", "email")

        
    def get_queryset(self):
        return Client.objects.all()

    """
    def get_queryset(self):
        first_name = self.request.query_params.get('first_name')
        email = self.request.query_params.get('email')
        if first_name is not None:
            return Client.objects.filter(first_name=first_name)
        elif email is not None:
            return Client.objects.filter(email=email)
        else:
            return Client.objects.all()
    """
    def list(self, request):
        print('////', request.user.role)
        if request.user.role == 'saler': # saler
            id_user = request.user.id
            clients = Client.objects.filter(sales_contact=id_user)
            print(clients)
            serializer = ClientSerializer(clients, many=True)
            return Response(serializer.data)
        elif request.user.role == 'technician': # technicien
            events = Event.objects.filter(support_contact=request.user.id)
            id_clients = []
            for event in events:
                id_clients.append(event.client.id)
            clients = Client.objects.filter(id__in=id_clients)
            serializer = ClientSerializer(clients, many=True)
            return Response(serializer.data)
        elif request.user.role == 'manager':
            clients = User.objects.all()
            serializer = UserSerializer(clients, many=True)
            return Response(serializer.data)
        

    def create(self, request, *args, **kwargs):
        request.POST._mutable = True  
        request.data["sales_contact"] = request.user.id
        request.POST_mutable = False 
        return super(ClientViewset, self).create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        request.POST._mutable = True
        id_client = kwargs['pk']
        client = Client.objects.get(id=id_client)
        request.data["email"] = client.email
        request.data["sales_contact"] = client.sales_contact.id
        request.POST_mutable = False
        return super(ClientViewset, self).update(request, *args, **kwargs)


@permission_classes([AllowAny,])
class RegisterApi(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            {
                "user": UserSerializer(user, context=self.get_serializer_context()).data,
                "message": "User Created Successfully. Now perform Login to get your token",
            }
        )