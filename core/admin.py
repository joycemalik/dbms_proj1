from django.contrib import admin
from .models import Severity, DisasterType, Cause, Location, Disaster, DisasterLocation, Impact, RecoveryShelter, Organisation, Aid

admin.site.register(Severity)
admin.site.register(DisasterType)
admin.site.register(Cause)
admin.site.register(Location)
admin.site.register(Disaster)
admin.site.register(DisasterLocation)
admin.site.register(Impact)
admin.site.register(RecoveryShelter)
admin.site.register(Organisation)
admin.site.register(Aid)
