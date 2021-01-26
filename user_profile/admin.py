from django.contrib import admin
from user_profile.models import Profile

# Register your models here.
# admin.site.register(Profile)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user','country', 'birth_date')
    search_fields = ('title',)
    list_editable = ('country',)