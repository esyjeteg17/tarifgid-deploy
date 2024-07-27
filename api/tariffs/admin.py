from .models import Tariff, Region
from django.contrib import admin

admin.site.register(Tariff)
""" admin.site.register(ModemTariff)
admin.site.register(HomephoneTariff)
admin.site.register(TVTariff)
admin.site.register(InternetTariff)
admin.site.register(SmartTariff) """
admin.site.register(Region)


