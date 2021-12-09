from rest_framework.permissions import BasePermission
from contract.models import Contract


METHODES_CREATE_READ = [ 'GET', 'POST']
METHODES_PUT_DEL = [ 'PUT', 'DELETE']


class IsManager(BasePermission):

	def has_permission(self, request, view):
		if request.user.role == 'manager':
			return True


class IsSalerContact(BasePermission):

	message = "L'utilisateur doit être le référent commercial du contrat"

	def has_permission(self, request, view): # obj
		if request.user.role == 'saler': 
			if request.method in METHODES_PUT_DEL:
				id_contract = view.kwargs['pk']
				contract = Contract.objects.get(id=id_contract)
				if contract.sales_contact.id == request.user.id :
					return True
			elif request.method in METHODES_CREATE_READ:
				if not view.kwargs:
					return True
				else:
					id_contract = view.kwargs['pk']
					contract = Contract.objects.get(id=id_contract)
					if contract.sales_contact.id == request.user.id :
						return True
		else:
			return False
