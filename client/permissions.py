from rest_framework.permissions import BasePermission
from client.models import Client


METHODES_CREATE_READ = [ 'GET', 'POST']
METHODES_PUT_DEL = [ 'PUT', 'DELETE']


class IsManager(BasePermission):

	def has_permission(self, request, view): # obj
		if request.user.role == 'manager':
			return True


class IsSalerContact(BasePermission):

	message = "L'utilisateur doit être le référent commercial du client"

	def has_permission(self, request, view): # obj
		if request.user.role == 'saler': 
			if request.method in METHODES_PUT_DEL:
				id_client = view.kwargs['pk']
				client = Client.objects.get(id=id_client)
				if client.sales_contact.id == request.user.id :
					return True
			elif request.method in METHODES_CREATE_READ:
				if not view.kwargs:
					return True
				else:
					id_client = view.kwargs['pk']
					client = Client.objects.get(id=id_client)
					if client.sales_contact.id == request.user.id :
						return True
		else:
			return False


class IsTechnicianEventContact(BasePermission):

	message = "L'utilisateur doit être le gestionnaire des events du client"

	def has_permission(self, request, view):
		if request.user.role == 'technician':
			if request.method == 'GET':
				return True
		else:
			return False

