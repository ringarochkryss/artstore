from django.contrib import admin
from .models import Order, OrderLineItem


"""
TabularInline subclass defines the template used to render
the Order in the admin interface. StackedInline is another option.
"""


class OrderLineAdminInline(admin.TabularInline):
    model = OrderLineItem


"""
The admin interface has the abilitiy to edit more than one model
on a single page. This is known as inlines.  
"""


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineAdminInline, )


admin.site.register(Order, OrderAdmin)
