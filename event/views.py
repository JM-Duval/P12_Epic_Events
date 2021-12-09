from rest_framework import viewsets
from event.models import Event
from event.serializers import EventSerializer
from client.models import Client
from client.serializers import ClientSerializer
from django_filters.rest_framework import DjangoFilterBackend
from event.permissions import IsSalerContact, IsTechnicianEventContact


class EventViewset(viewsets.ModelViewSet):

    permission_classes = [ IsSalerContact  | IsTechnicianEventContact ]
    serializer_class = EventSerializer
    queryset = Event.objects.all()
    http_method_names = ['get', 'post', 'delete', 'put']
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ("client__first_name", "client__email", "event_date")
    

    def get_queryset(self):
        return Event.objects.all()








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
        
        test = Event.objects.filter(client=1)
        print(test)
        #print(test.strftime("%b %d %Y"))

        if first_name is not None:
            id_client = self.get_id_client_with_first_name(first_name)
            return Event.objects.filter(client=id_client)
        elif email is not None:
            id_client = self.get_id_client_with_email(email)     
            return Event.objects.filter(client=id_client)
        elif date is not None:
            return Event.objects.filter(date_created=date)
        else:
            return Event.objects.all() 
    """