from django.contrib import admin
from .models import Client, User
from django import forms


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
	list_display = ('first_name', 'last_name', 'email',
	 'company_name', 'sales_contact')


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username", "password", "first_name", "last_name", "role", "is_admin")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
	

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    form = UserForm

    list_display = ('first_name', 'last_name', 'username', 'role', 'password', "is_admin")
    list_filter = ("role",)

"""
class UserAdmin(admin.ModelAdmin):
	list_display = ('first_name', 'last_name', 'username', 'role', 'password')

admin.site.register(User, UserAdmin)
"""


