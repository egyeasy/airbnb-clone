from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# Register your models here.
@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """ Custom User Admin """

    # 기존의 fieldset과 합쳐준다.
    fieldsets = UserAdmin.fieldsets + \
                (
                    (
                        "Custom Profile",
                        {
                            "fields": (
                                "avatar",
                                "gender",
                                "bio",
                                "birthdate",
                                "language",
                                "currency",
                                "superhost",
                            )
                        },
                    ),
                )
