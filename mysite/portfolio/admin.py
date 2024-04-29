# Register your models here.

from django.contrib import admin

from .models import Portfolio, Blog, Blog_Category, Web_Services, Feedback, Mobile_Services, Desktop_Services


class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('category', 'client', 'project_date', 'project_url')


admin.site.register(Portfolio, PortfolioAdmin)

admin.site.register(Blog_Category)
admin.site.register(Blog)
admin.site.register(Web_Services)
admin.site.register(Mobile_Services)
admin.site.register(Desktop_Services)
admin.site.register(Feedback)
