from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User



class DownloadableUserAdmin(UserAdmin):

    actions = ['download_csv']

    def download_csv(self, request, queryset):
        import csv
        from django.http import HttpResponse
        import StringIO
     
        f = StringIO.StringIO()
        writer = csv.writer(f)
        writer.writerow(["first_name", "last_name", "email", "username"])
     
        for s in queryset:
            writer.writerow([s.first_name, s.last_name, s.email, s.username])
     
        f.seek(0)
        response = HttpResponse(f, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; sanctuary-users.csv'
        return response
    download_csv.short_description = 'Download CSV'

admin.site.unregister(User)
admin.site.register(User, DownloadableUserAdmin)

