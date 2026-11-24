import csv
from django.http import HttpResponse
from django.contrib import admin
from newsletter.models import Subscriber
# Register your models here.

class SubscriberAdmin(admin.ModelAdmin):
    actions = ['export_subscribers']
    def export_subscribers(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="subscribers.csv"'
        writer = csv.writer(response)
        writer.writerow(['Email', 'Is Active', 'Created At'])
        for subscriber in queryset:
            writer.writerow([
                subscriber.email,
                subscriber.is_active,
                subscriber.created_at
            ])
        return response

admin.site.register(Subscriber, SubscriberAdmin)
