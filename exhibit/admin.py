from django.contrib import admin
from .models import Gallery, GalleryArtist, GalleryArt 


"""
TabularInline subclass defines the template used to render
the Order in the admin interface. StackedInline is another option.
"""
class GalleryAdmin(admin.ModelAdmin):
    model = GalleryArt

class GalleryArtAdmin(admin.ModelAdmin):
    model = GalleryArt

class GalleryArtistAdmin(admin.ModelAdmin):
    model = GalleryArtist

class GalleryArtAdminInline(admin.TabularInline):
    model = GalleryArt


admin.site.register(Gallery, GalleryAdmin)
admin.site.register(GalleryArt, GalleryArtAdmin)
admin.site.register(GalleryArtist, GalleryArtistAdmin)