from .forms import UserCreationForm, UserChangeForm
from .models import User,Courses,Student
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


class UserAdmin(UserAdmin):
	add_form = UserCreationForm
	form = UserChangeForm
	model = User
	list_display = ('username', 'name', 'email', 'is_active')
	list_filter = ('username', 'name', 'email', 'is_active')
	fieldsets = (
		(None, {'fields': ('name', 'username', 'email', 'password')}),
		('Permissions', {'fields': ('is_staff', 'is_active')})
	)
	search_fields = ('username',)
	ordering = ('username',)
    
admin.site.register(User, UserAdmin)
admin.site.register(Courses)
admin.site.register(Student)