from django.contrib import admin
from notifications import models
# Register your models here.

admin.site.register(models.FCMDevice)
admin.site.register(models.Notification)