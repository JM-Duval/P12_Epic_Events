from rest_framework import viewsets
from event.models import Event
from event.serializers import EventSerializer
from client.models import Client
from client.serializers import ClientSerializer
from django_filters.rest_framework import DjangoFilterBackend
from event.permissions import IsSalerContact, IsTechnicianEventContact, IsManager


class EventViewset(viewsets.ModelViewSet):

    permission_classes = [ IsSalerContact  | IsTechnicianEventContact |
                           IsManager ]
    serializer_class = EventSerializer
    queryset = Event.objects.all()
    http_method_names = ['get', 'post', 'delete', 'put']
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ("client__first_name", "client__email", "event_date")
    

    def get_queryset(self):
        return Event.objects.all()

