from django.contrib import admin
from .models import Client, User

class ClientAdmin(admin.ModelAdmin):
	list_display = ('first_name', 'last_name', 'email',
	 'company_name', 'sales_contact')

admin.site.register(Client, ClientAdmin)


class UserAdmin(admin.ModelAdmin):
	list_display = ('first_name', 'last_name', 'username', 'role')

admin.site.register(User, UserAdmin)
