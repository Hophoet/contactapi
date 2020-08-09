from django.contrib import admin
#models
from .models import (Client, Company)

#registration of models
admin.site.register(Client)
admin.site.register(Company)