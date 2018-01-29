from django.contrib import admin
from activity import models

admin.site.register(models.Category)
admin.site.register(models.Activity)
admin.site.register(models.ResponseToActivity)
