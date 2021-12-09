from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from contract.models import Contract


class ContractSerializer(ModelSerializer):
	date_created = serializers.DateField(format="%d-%m-%Y")
	payment_due = serializers.DateField(format="%d-%m-%Y")
	class Meta:
		model = Contract
		fields = ['id', 'sales_contact', 'client', 'status', 'amount',
			'date_created', 'payment_due']
