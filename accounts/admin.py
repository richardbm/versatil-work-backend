from django.contrib import admin
from accounts import models
# Register your models here.

admin.site.register(models.User)
admin.site.register(models.RatingSupply)
admin.site.register(models.RatingDemand)
admin.site.register(models.Token)
