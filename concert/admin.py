from django.contrib import admin
from .models import Concert, ConcertAttending

# Register the Concert model with the admin site
admin.site.register(Concert)

# Optionally, you can customize how the ConcertAttending model is displayed in the admin
class ConcertAttendingAdmin(admin.ModelAdmin):
    list_display = ('concert', 'user', 'attending')
    list_filter = ('attending',)
    search_fields = ('user__username', 'concert__concert_name')

# Register the ConcertAttending model with the custom admin class
admin.site.register(ConcertAttending, ConcertAttendingAdmin)
