"""Template tags for the object_faq app."""
from django import template
from django.contrib.contenttypes.models import ContentType

from ..models import Entry, GlobalObjectDescription

register = template.Library()


@register.inclusion_tag('object_faq/partials/object_faq.html',
                        takes_context=True)
def render_faq_for_object(context, obj):
    ctype = ContentType.objects.get_for_model(obj.__class__)
    try:
        globalobjectdescription = GlobalObjectDescription.objects.get(
            content_type=ctype, object_id=obj.id)
    except GlobalObjectDescription.DoesNotExist:
        globalobjectdescription = None
    faqs = Entry.objects.filter(content_type=ctype, object_id=obj.id)
    return {'globalobjectdescription': globalobjectdescription, 'faqs': faqs}
