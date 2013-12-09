"""Factories for the object_faq app."""
from django.contrib.contenttypes.models import ContentType

import factory
from django_libs.tests.factories import HvadFactoryMixin, UserFactory

from ..models import Entry, GlobalObjectDescription


class EntryFactory(HvadFactoryMixin, factory.DjangoModelFactory):
    """Factory for the ``Entry`` model."""
    FACTORY_FOR = Entry

    object = factory.SubFactory(UserFactory)
    content_type = factory.LazyAttribute(
        lambda e: ContentType.objects.get_for_model(e.object.__class__))
    object_id = factory.LazyAttribute(lambda e: e.object.id)
    question = factory.Sequence(lambda n: 'question {0}'.format(n))


class GlobalObjectDescriptionFactory(HvadFactoryMixin,
                                     factory.DjangoModelFactory):
    """Factory for the ``GlobalObjectDescription`` model."""
    FACTORY_FOR = GlobalObjectDescription

    object = factory.SubFactory(UserFactory)
    content_type = factory.LazyAttribute(
        lambda e: ContentType.objects.get_for_model(e.object.__class__))
    object_id = factory.LazyAttribute(lambda e: e.object.id)
    content = factory.Sequence(lambda n: 'content {0}'.format(n))
