from django.contrib import admin
from .models import Custom_user


# Register your models here.


class admin_custom_user(admin.ModelAdmin):
    list_display = ['user', 'phone']
    search_fields = ['user']

    class Meta:
        model = Custom_user


admin.site.register(Custom_user, admin_custom_user)
