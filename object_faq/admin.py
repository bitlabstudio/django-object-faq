"""Admin classes for the object_faq app."""
from django.contrib import admin

from hvad.admin import TranslatableAdmin

from .models import Entry, GlobalObjectDescription


admin.site.register(Entry, TranslatableAdmin)
admin.site.register(GlobalObjectDescription, TranslatableAdmin)
