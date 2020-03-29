from django.contrib import admin
from .models import Gallery, GalleryArtist, GalleryArt 


"""
TabularInline subclass defines the template used to render
the Order in the admin interface. StackedInline is another option.
"""


class GalleryArtAdminInline(admin.TabularInline):
    model = GalleryArt

class GalleryArtAdmin(admin.ModelAdmin):
    model = GalleryArt


"""
The admin interface has the abilitiy to edit more than one model
on a single page. This is known as inlines.  
"""


class GalleryAdmin(admin.ModelAdmin):
    inlines = (GalleryArtAdminInline, )

class GalleryArtAdmin(admin.ModelAdmin):
    model = GalleryArt

admin.site.register(Gallery, GalleryAdmin)
admin.site.register(GalleryArt, GalleryArtAdmin)
admin.site.register(GalleryArtist)