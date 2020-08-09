from django.contrib import admin
#models
from .models import (Client, Company)

#registring
admin.site.register(Client)
admin.site.register(Company)