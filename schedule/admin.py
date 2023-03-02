from django.contrib import admin
from .models import Availability, Schedule, TeamMeeting

admin.site.register(Availability)
admin.site.register(Schedule)
admin.site.register(TeamMeeting)
